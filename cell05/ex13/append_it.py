#!/usr/bin/env python3
import sys

arguments = sys.argv[1:]

if len(arguments) == 0:
    print("none")
else:

    for arg in arguments:

        if not arg.endswith("ism"):

            print(arg + "ism")
