#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Regex for a valid ID number
pattern = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'

# Now validate each ID number
for id_number in lines[1:]:
    if re.match(pattern, id_number):
        print("VALID")
    else:
        print("INVALID")
