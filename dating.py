#!/usr/bin/env python3
# Created by: Alex OBrien
# Created on: October 27, 2026
# This program is a dating acceptance program
# run by the grandparents of the date
# to either accept or deny dating applicants

user_input = input("Enter your age: ")

try:
    age = int(user_input)

    # Check for invalid/unrealistic age values
    if age < 0 or age > 120:
        print("Please enter your true age!")
    # Check if age is greater than 25 AND less than 40
    elif age > 25 and age < 40:
        print("You can date my grandchild!")
    else:
        print("You’re too young to date my grandchild!")

except ValueError:
    print(f"{user_input} is not a valid input!")
