#lets say you need to check some data types to make sure they are the correct data type before you can use them in your program.
#  example, you want to make sure that the user input is a number before you can use it in your program. 
# You can use the isinstance() function to check the data type of a variable.

while True:
    age = input("Please enter your age: ")

    if age.isdigit():
        age = int(age)
        print(f"Your age is {age}")
        break
    else:
        print("Please enter a valid number for your age.")
        