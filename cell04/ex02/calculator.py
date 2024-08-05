#!/usr/bin/env python3
first_number_input = input("Give me the first number: ")
second_number_input = input("Give me the second number: ")

try:
    first_number = float(first_number_input)
    second_number = float(second_number_input)

    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    division = first_number / second_number if second_number != 0 else 'undefined'

    print("Thank you!")
    print(f"{first_number} + {second_number} = {addition}")
    print(f"{first_number} - {second_number} = {subtraction}")
    print(f"{first_number} / {second_number} = {division}")
    print(f"{first_number} * {second_number} = {multiplication}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
