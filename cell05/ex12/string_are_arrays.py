#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:

    input_string = sys.argv[1]

    z_characters = [char for char in input_string if char == 'z']

    if not z_characters:
        print("none")
    else:
        print(''.join(z_characters))
