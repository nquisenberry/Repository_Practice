# if else statements are dual alternatives, meaning that if the condition is true, 
# the code block under the if statement will execute. 
# If the condition is false, the code block under the else 
# statement will execute. The basic syntax of an if else statement in 
# Python is as follows:

#example of an if else statement to accept terms and conditions
terms_and_conditions = input("Do you accept the terms and conditions? (yes/no): ")

if terms_and_conditions == "yes":
    print("You have accepted the terms and conditions")
else:
    print("You have not accepted the terms and conditions") 

#checking to see if you are old enough to vote

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote")
    