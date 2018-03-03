#!/usr/bin/env python3

import re
import sys


# Given in the problem statement
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
instring = lines[1]

# Give answer
has_number = False
has_lower_case = False
has_upper_case = False
has_special_character = False

for lett in instring:
    if lett in numbers:
        has_number = True
    elif lett in lower_case:
        has_lower_case = True
    elif lett in upper_case:
        has_upper_case = True
    elif lett in special_characters:
        has_special_character = True

nots = (int(not has_number)
       + int(not has_lower_case)
       + int(not has_upper_case)
       + int(not has_special_character))

diff_six = 6 - len(instring)

print(max(nots, diff_six))
