#!/usr/bin/env python3

user_input = input("Enter a number: ")

try:
    number = float(user_input)

    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
