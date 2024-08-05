#!/usr/bin/env python3
import sys


arguments = sys.argv[1:]


if len(arguments) == 0:
    print("none")
else:

    print(f"parameters: {len(arguments)}")
    
    for arg in arguments:
        print(f"{arg}: {len(arg)}")
