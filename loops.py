#loops are part of programming that allow you to execute a block of code multiple times.
#
# 
# while loops are used to repeat a block of code as long as a condition is true. 
#for loops are used to iterate over a sequence (such as a list, tuple, or string) 
# and execute a block of code for each item in the sequence. 

#while loops are usually broken by a flag or a sentinel value, which is a value
#  that indicates when the loop should stop.

#flag value
keep_going = "y"

#make a commission program that checks sales and comission rates. breaks 
#when the user enters "n" for no more sales.

while keep_going == "y":
    sales = float(input("Please enter the sales amount: "))
    commission_rate = 0.1
    commission = sales * commission_rate
    print(f"Your commission is: ${commission:.2f}")
    keep_going = input("Do you have more sales to enter? (y/n): ")

else:
    print("Thank you for using the commission program.")
    