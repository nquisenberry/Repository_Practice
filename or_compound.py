#or condition means that at least one of the conditions must be true for the 
# code block to execute.

#tickets at a theseaters are $10 for adults and $5 for 
# children under 7. If you are a senior citizen, you get a discount and your ticket is $7.

age = int(input("Please enter your age: "))

#make sure even though we will be using one variable, we will be using two conditions
# to check if the person is eligible for a discount or not.
#if age < 18 or age >= 65: 

if age < 7 or age >= 65:
    print("You are eligible for a discount")
else:
    print("You are not eligible for a discount")
        
