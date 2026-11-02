#compound conditionals allow you to combine multiple conditions in a single if statement. 
# You can use logical operators such as "and", "or", and "not" to create complex 
# conditions.

#and = both conditions must be true for the code block to execute
#or = at least one condition must be true for the code block to execute
#not = reverses the boolean value of the condition, if the condition is true, 
# it will become false and vice versa.

#and compund conditional voting example using the and operator

age = int(input("Please enter your age: "))
us_citizen = input("Are you a U.S. citizen? (yes/no): ")

if age >= 18 and us_citizen == "yes":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")   


