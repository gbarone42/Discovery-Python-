#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
    sys.exit()


keyword = sys.argv[1]
text = sys.argv[2]

occurrences = re.findall(re.escape(keyword), text)


if not occurrences:
    print("none")
else:

    print(len(occurrences))
