# if we want to make our own function, (custom or defined) we can define or create a template for it. 
# in python we call these defined functions

# functions can be defined in several ways
# functions in programming are a seres of statements thant can be called with a keyword, CAN take input
# process data and return output

# the following are examples of ways you can use a function

# characteristic 1 - a functinon can be a series of statements tied to a keyword you make
# to definr a function we just say def function_name()

# the power of functions becomes apparent when we use parameters
# parameters are treates like placeholderes for incoming data

# reminder!! arguments are what we use to call/running a function, parameters are placeholders for defined
# functions

# syntax - def function_name(parameter)
# in python we can pass any data type we want into the function including lists and dictionaries.
# in oython we can also apss data from one funtion to another.

def happy_birthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday dear", name)
    print("Happy birthday to you!")

myname = input("give me your name ")

happy_birthday(myname)