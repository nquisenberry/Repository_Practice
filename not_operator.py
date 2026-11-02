#not operator by itself does not create a compound conditional, 
# but it can be used to reverse the boolean value of a condition. 

x = 15

# not's are often used with other compund operators to get a result that is the opposite of what you would normally expect.

#for instance, I want to see if x is not equal to 11 or 12, I can use the not 
# operator to reverse the boolean value of the condition.

if not(x == 11 or x == 12):
    print("x is not equal to 11 or 12")

else:
    print("x is equal to 11 or 12")