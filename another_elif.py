#elif statements are multiple alternatives that can have mre than one branch of code 
# to execute based on different conditions. The basic syntax of an elif
#  statement in Python is as follows:

#below is a progran to convert a nemurical grade to a letter grade using an elif statement. The program will ask the user to input a numerical grade and then convert it to a letter grade based on the following scale:
# A = 90-100   
# B = 80-89
# C = 70-79
# D = 60-69
# F = 0-59  

number_grade = 82
letter_grade = ""

# short circt evaluation is used in the elif statement, meaning that if the first 
# condition is true, the rest of the conditions will not be evaluated. 
# This is important to note because it can affect the outcome of the program if the 
# conditions are not ordered correctly.

if number_grade >= 90:
    letter_grade = "A"
elif number_grade >= 80:
    letter_grade = "B"
elif number_grade >= 70:
    letter_grade = "C"
elif number_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your letter grade is: {letter_grade}")