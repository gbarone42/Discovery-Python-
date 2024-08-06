#!/usr/bin/env python3
import sys

def downcase_it(s):
    return s.lower()

arguments = sys.argv[1:]

if len(arguments) == 0:
    print("none")
else:

    for arg in arguments:
        print(downcase_it(arg))
