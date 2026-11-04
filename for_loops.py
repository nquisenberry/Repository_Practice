#for loops are loops that repeat a block of code a certain number of times.
#  They are commonly used to iterate over sequences such as lists, tuples, or strings.

#for (int i = 0; i < 10; i++) {
#    print(i)

#where i represents the loop variable, which is initialized to 0 and incremented by 
# 1 on each iteration until it reaches 10.

#what python does differently is that it uses the range() function to generate a sequence of 
# numbers, and the loop variable is automatically assigned to each value in the sequence.    

#syntax for a in loop - for i in range(start, stop, step):

number = 5 
for i in range(0, number, 1):  # range(start, stop, step) - start is inclusive, stop is exclusive           
    print(i)  # prints numbers from 0 to 4


print("**************" )

#we can also shorthand the for in range loop if we know we want to start at 0 and increment by 1, we can just use range(stop) instead of range(start, stop, step)
for i in range(number):  # shorthand for range(0, number, 1)
    print(i)  # prints numbers from 0 to 4  


print("**************" )

#we can also count down using negative step values in the range() function. For example, to count down from 5 to 1, we can use the following code:

for i in range(5, 0, -1):  # counts down from 5 to 1
    print(i)  # prints numbers from 5 to 1
    
    
print("**************" )

#we can set our increment step to any value we want, for example, to count by 2's from 0 to 10, we can use the following code:

for i in range(0, 11, 2):  # counts by 2
    print(i)  # prints 0, 2, 4, 6, 8, 10  

print("**************" )  
