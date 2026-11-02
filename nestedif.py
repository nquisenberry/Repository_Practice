#nested if statements work by having to meet multiple conditions in order
#  for the code block to execute. The basic syntax of a nested if statement
#  in Python is as follows:

#we will use voting for a u.s citizen as an example of a nested if statement. In order to vote in the u.s you must be a citizen and be 18 years or older.

age = int(input("Please enter your age: "))

if age >= 18:
    us_citizen = input("Are you a U.S. citizen? (yes/no): ")
    if us_citizen == "yes":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote because you are not a U.S. citizen")    
else:
    print("You are not eligible to vote because you are not 18 years or older")
            