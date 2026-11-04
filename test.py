# Name: Nathan Quisenberry
# File Name: student_honor_roll.py
# File Name: student_gpa.py
# Description: This program accepts student names and GPAs,
# then determines whether the student qualifies for the
# Dean's List or the Honor Roll.
#
# Variables:
# last_name - stores the student's last name
# first_name - stores the student's first name
# gpa - stores the student's GPA as a floating-point number

while True:
    # Get student's last name
    last_name = input("Enter student's last name (or ZZZ to quit): ")

    # Exit program if ZZZ is entered
    if last_name.upper() == "ZZZ":
        print("Program terminated.")
        break

    # Get student's first name
    first_name = input("Enter student's first name: ")

    # GPA validation
    while True:
        try:
            gpa = float(input("Enter student's GPA: "))

            if gpa < 0.0 or gpa > 4.0:
                print("Error: GPA must be between 0.0 and 4.0.")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid numeric GPA.")

    # Check for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")

    # Check for Honor Roll
    if gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")

    print()