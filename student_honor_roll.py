#Name: Addison Kopp
#File name: student_honor_roll.py
#Description: This program accepts students names and GPAs and determines where the student qualifies for the Dean's List or the Honor Roll. 
last_name = input("Enter the student's last name (ZZZ to quit):")

while last_name != "ZZZ":
    first_name = input("Enter the student's first name:")
    gpa = float(input("Enter the student's GPA:"))
    
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")

    last_name = input("Enter the student's last name (ZZZ to quit):")