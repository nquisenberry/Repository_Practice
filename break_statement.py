#sometimes we want to break out of a loop when a certain condition is met. 
# In Python, we can use the break statement to do this. The break statement allows us 
# to exit a loop prematurely, regardless of whether the loop's condition is still true.

#the break keyword can be used in both while and for loops. When the break statement 
# is executed, the loop will terminate immediately, and the program will continue 
# executing the code that follows the loop.

#instead we can say while True: and then use the break statement to exit the loop 
# when a certain condition is met.

while True:
    accept = input("Do you accept the terms and conditions? press y and enter to accept or n and enter to decline: ")

    if accept == "y":
        print("You have accepted the terms and conditions")
        break
    elif accept == "n":
        print("You have not accepted the terms and conditions")
        break

print("Thank you for using Nate's program.")