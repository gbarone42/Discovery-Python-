#!/usr/bin/env python3

# Prompt the user for a number
number_input = input("Give me a number: ")

try:
    number = float(number_input)

    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
