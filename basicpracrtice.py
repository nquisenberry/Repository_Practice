#if statements in python are single alternatives, meaning that if the condition is true, the code block under the if statement will execute. If the condition is false, the code block will be skipped.
#and allow you to create branches in your code, allowing you to execute different code blocks based on different conditions.
#they relay rational operators to compare values and make decisions based on those comparisons. The basic syntax of an if statement in Python is as follows:

#lets look to create an if statement to see if two values are equal
#if statements do not have to use () or {} to define the code block, instead they use indentation to define the code block. The code block under the if statement will be indented by four spaces or one tab.
#syntax is if conditon
#following by a colon and then the code block indented under the if statement.

#if true run code 

a = 5
b = 5

if a == b:
    print("a and b are equal")  

#greater than or equal to
c = 6
d = 5

if d <= c:
    print("d is less than or equal to c")       

#can also use strings
us_citizen = "yes"

if us_citizen == "yes":
    print("You are a US citizen")   

#boolean values can also be used in if statements, where True and False are the only two possible values.
myboolean_true = True   
myboolean_false = False

if myboolean_true:
    print("The boolean value is True")

if myboolean_false:
    print("The boolean value is False")     

