#we can use loops as accumulators (running totals)
#this program is a program that averages numbers.

#average = total / count    

sum = 0  # accumulator variable to hold the sum of numbers
count = 0  # accumulator variable to hold the count of numbers  

#we dcan have users control loop values by asking for input from the user. 
# For example, we can ask the user how many numbers they want to average, 
# and then use that value to control the loop.

how_many_numbers = int(input("How many numbers do you want to average? ")) 

#wa can use either loop for this but I would use a for loop.

for i in range(how_many_numbers):  # loop will run how_many_numbers times
    number = float(input("Enter a number you wish to average: "))  # get a number from the user
#accumulate the sum and count of numbers    
    sum += number  # add the number to the sum

    print(f"Current sum: {sum}")  # print the current sum

average = sum / how_many_numbers  # calculate the average
print(f"The average of the {how_many_numbers} numbers is: {average}")  #


    