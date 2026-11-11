# classes can represent real world objects and behavior that can be modified or changed

# lets create sa class called dog with the attributes name, age, and animal 
# dog will always have class variable dog. 
# but every dog will have a different name

class Dog:
    animal = "dog"

    def __init__(self,name,age):
        self.name = name
        self.age = age


dog1 = Dog("Nala",10)
print(dog1.name)
print(dog1.age)
print(dog1.animal)
