#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        range_array = list(range(start, end + 1))
        
        print(range_array)
    except ValueError:
        print("none")
