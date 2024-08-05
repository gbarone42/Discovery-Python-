#!/usr/bin/env python3

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    for i in range(10):
        result = i * number
        print("%d x %d = %d" % (i, number, result))
except ValueError:
    print("Invalid input. Please enter a valid number.")
