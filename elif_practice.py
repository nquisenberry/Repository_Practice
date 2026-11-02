#ask your customer what their name is with the inout() function and store in the variable name
name = input("What is your name?\n ")

if name == "Nathaniel":
    evil_status = input("Are you evil? \n")
    if evil_status == "yes":
        print("You are evil, " + name + "!")
    else:
        print("You are not evil, " + name + "!")
else:
    print("You are not Alice or Bob, come on in! " + name + "!")