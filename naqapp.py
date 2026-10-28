"""A small, persistent command-line inventory application."""

from __future__ import annotations

import hashlib
import hmac
import json
import math
import os
import secrets
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).resolve().parent
USERS_FILE = DATA_DIR / "users.json"
INVENTORY_FILE = DATA_DIR / "inventory.json"
PASSWORD_ITERATIONS = 200_000


def _read_json(path: Path, default: Any) -> Any:
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.name} contains invalid JSON") from error


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump(data, file, indent=2)
            file.write("\n")
        os.replace(temporary_path, path)
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


@dataclass(frozen=True)
class User:
    username: str
    salt: str
    password_hash: str


class AuthManager:
    def __init__(self, users_file: Path = USERS_FILE) -> None:
        self.users_file = Path(users_file)
        records = _read_json(self.users_file, [])
        if not isinstance(records, list):
            raise ValueError("users.json must contain a JSON list")
        self.users: dict[str, User] = {}
        for record in records:
            if not isinstance(record, dict):
                raise ValueError("users.json contains an invalid user record")
            try:
                user = User(
                    username=record["username"],
                    salt=record["salt"],
                    password_hash=record["password_hash"],
                )
            except KeyError as error:
                raise ValueError("users.json contains an incomplete user record") from error
            if not all(isinstance(value, str) for value in (user.username, user.salt, user.password_hash)):
                raise ValueError("users.json contains an invalid user record")
            try:
                salt_bytes = bytes.fromhex(user.salt)
                hash_bytes = bytes.fromhex(user.password_hash)
            except ValueError as error:
                raise ValueError("users.json contains an invalid user record") from error
            if not user.username or len(salt_bytes) != 16 or len(hash_bytes) != 32:
                raise ValueError("users.json contains an invalid user record")
            if user.username in self.users:
                raise ValueError("users.json contains duplicate usernames")
            self.users[user.username] = user

    def register(self, username: str, password: str) -> User:
        username = username.strip()
        if not username:
            raise ValueError("Username cannot be empty.")
        if username in self.users:
            raise ValueError("That username is already registered.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        salt = secrets.token_hex(16)
        password_hash = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), bytes.fromhex(salt), PASSWORD_ITERATIONS
        ).hex()
        user = User(username, salt, password_hash)
        updated_users = [*self.users.values(), user]
        _write_json(
            self.users_file,
            [
                {
                    "username": item.username,
                    "salt": item.salt,
                    "password_hash": item.password_hash,
                }
                for item in updated_users
            ],
        )
        self.users[username] = user
        return user

    def authenticate(self, username: str, password: str) -> User | None:
        user = self.users.get(username.strip())
        if user is None:
            return None
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(user.salt),
            PASSWORD_ITERATIONS,
        ).hex()
        return user if hmac.compare_digest(password_hash, user.password_hash) else None


@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    quantity: int
    price: float


class Inventory:
    def __init__(self, inventory_file: Path = INVENTORY_FILE) -> None:
        self.inventory_file = Path(inventory_file)
        records = _read_json(self.inventory_file, [])
        if not isinstance(records, list):
            raise ValueError("inventory.json must contain a JSON list")
        self.products: dict[int, Product] = {}
        for record in records:
            if not isinstance(record, dict):
                raise ValueError("inventory.json contains an invalid product record")
            try:
                product_id = record["product_id"]
                name = record["name"]
                quantity = record["quantity"]
                price = record["price"]
            except KeyError as error:
                raise ValueError("inventory.json contains an incomplete product record") from error
            if isinstance(price, bool) or not isinstance(price, (int, float)):
                raise ValueError("inventory.json contains an invalid product record")
            try:
                product = Product(
                    product_id=product_id,
                    name=name,
                    quantity=quantity,
                    price=float(price),
                )
            except (OverflowError, ValueError) as error:
                raise ValueError("inventory.json contains an invalid product record") from error
            if (
                isinstance(product.product_id, bool)
                or not isinstance(product.product_id, int)
                or product.product_id < 1
                or not isinstance(product.name, str)
                or not product.name.strip()
                or isinstance(product.quantity, bool)
                or not isinstance(product.quantity, int)
                or product.quantity < 0
                or isinstance(product.price, bool)
                or not isinstance(product.price, (int, float))
                or not math.isfinite(product.price)
                or product.price < 0
                or product.product_id in self.products
            ):
                raise ValueError("inventory.json contains an invalid product record")
            self.products[product.product_id] = product

    def list_products(self) -> list[Product]:
        return sorted(self.products.values(), key=lambda product: product.product_id)

    def add_product(self, name: str, quantity: int, price: float) -> Product:
        name = name.strip()
        if not name:
            raise ValueError("Product name cannot be empty.")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative whole number.")
        if (
            isinstance(price, bool)
            or not isinstance(price, (int, float))
            or not math.isfinite(price)
            or price < 0
        ):
            raise ValueError("Price must be a finite, non-negative number.")

        product_id = max(self.products, default=0) + 1
        product = Product(product_id, name, quantity, float(price))
        self._save([*self.products.values(), product])
        self.products[product_id] = product
        return product

    def adjust_stock(self, product_id: int, change: int) -> Product:
        if isinstance(change, bool) or not isinstance(change, int):
            raise ValueError("Stock change must be a whole number.")
        product = self._get_product(product_id)
        quantity = product.quantity + change
        if quantity < 0:
            raise ValueError("Not enough stock for that operation.")
        updated = Product(product.product_id, product.name, quantity, product.price)
        self._save(
            [updated if item.product_id == product_id else item for item in self.products.values()]
        )
        self.products[product_id] = updated
        return updated

    def remove_product(self, product_id: int) -> None:
        self._get_product(product_id)
        updated_products = [
            product for product in self.products.values() if product.product_id != product_id
        ]
        self._save(updated_products)
        del self.products[product_id]

    def _get_product(self, product_id: int) -> Product:
        if isinstance(product_id, bool) or not isinstance(product_id, int):
            raise ValueError("Product ID must be a whole number.")
        try:
            return self.products[product_id]
        except KeyError as error:
            raise ValueError(f"No product exists with ID {product_id}.") from error

    def _save(self, products: list[Product]) -> None:
        _write_json(
            self.inventory_file,
            [
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "quantity": product.quantity,
                    "price": product.price,
                }
                for product in products
            ],
        )


def _read_integer(prompt: str, minimum: int = 0) -> int:
    try:
        value = int(input(prompt))
    except ValueError as error:
        raise ValueError("Enter a whole number.") from error
    if value < minimum:
        raise ValueError(f"Enter a number no smaller than {minimum}.")
    return value


def _read_price() -> float:
    try:
        price = float(input("Price: "))
    except ValueError as error:
        raise ValueError("Enter a valid price.") from error
    if not math.isfinite(price) or price < 0:
        raise ValueError("Price must be a finite, non-negative number.")
    return price


def _show_products(inventory: Inventory) -> None:
    products = inventory.list_products()
    if not products:
        print("No products in inventory.")
        return
    print("\nID  Product                         Quantity  Price")
    print("-" * 58)
    for product in products:
        print(f"{product.product_id:<3} {product.name:<31.31} {product.quantity:>8}  ${product.price:.2f}")


def _inventory_menu(inventory: Inventory) -> None:
    while True:
        print(
            "\nInventory"
            "\n1. List products"
            "\n2. Add product"
            "\n3. Restock product"
            "\n4. Sell product"
            "\n5. Remove product"
            "\n6. Log out"
        )
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                _show_products(inventory)
            elif choice == "2":
                name = input("Product name: ")
                quantity = _read_integer("Starting quantity: ")
                price = _read_price()
                product = inventory.add_product(name, quantity, price)
                print(f"Added {product.name} with ID {product.product_id}.")
            elif choice in {"3", "4"}:
                product_id = _read_integer("Product ID: ", minimum=1)
                amount = _read_integer("Quantity: ", minimum=1)
                product = inventory.adjust_stock(
                    product_id, amount if choice == "3" else -amount
                )
                action = "Restocked" if choice == "3" else "Sold"
                print(f"{action} {amount} unit(s). {product.quantity} now in stock.")
            elif choice == "5":
                product_id = _read_integer("Product ID to remove: ", minimum=1)
                inventory.remove_product(product_id)
                print("Product removed.")
            elif choice == "6":
                return
            else:
                print("Choose an option from 1 to 6.")
        except ValueError as error:
            print(f"Error: {error}")
        except OSError as error:
            print(f"Could not save your changes: {error}")


def main() -> None:
    try:
        auth = AuthManager(USERS_FILE)
        inventory = Inventory(INVENTORY_FILE)
        while True:
            print("\nInventory Project\n1. Log in\n2. Register\n3. Exit")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                user = auth.authenticate(username, password)
                if user is None:
                    print("Invalid username or password.")
                else:
                    print(f"Welcome, {user.username}.")
                    _inventory_menu(inventory)
            elif choice == "2":
                username = input("Choose a username: ")
                password = input("Choose a password (at least 8 characters): ")
                try:
                    user = auth.register(username, password)
                except (OSError, ValueError) as error:
                    print(f"Registration failed: {error}")
                    continue
                print(f"Account created. Welcome, {user.username}.")
                _inventory_menu(inventory)
            elif choice == "3":
                print("Goodbye.")
                return
            else:
                print("Choose 1, 2, or 3.")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye.")
    except (OSError, ValueError) as error:
        print(f"Unable to start the inventory application: {error}")


if __name__ == "__main__":
    main()