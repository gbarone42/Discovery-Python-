#!/usr/bin/env python3
import sys


arguments = sys.argv[1:]

if len(arguments) < 2:
    print("none")
else:
    for arg in reversed(arguments):
        print(arg)
