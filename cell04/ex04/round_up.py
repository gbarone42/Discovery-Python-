#!/usr/bin/env python3
import math


number_input = input("Give me a number: ")

try:

    number = float(number_input)

    rounded_number = math.ceil(number)

    print(rounded_number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
