#!/usr/bin/env python3

import re
import sys

LOW_X_LIM = -90
HIGH_X_LIM = 90
LOW_Y_LIM = -180
HIGH_Y_LIM = 180


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Pattern to match coordinates
number_pattern = (r'('
                  + r'(?:[+-]?[1-9]\d*(?:\.\d+)?)'
                  + r'|'
                  + r'(?:[+-]?0(?:\.\d+)?)'
                  + r'|'
                  + r'(?:[+-]?\.\d+)'
                  + r')')
full_pattern = (r'\('
                + number_pattern
                + r', '
                + number_pattern
                + r'\)')

# Go through each coordinate and validate
for pair in lines[1:]:
    matches = re.match(full_pattern, pair)

    if matches:
        if (LOW_X_LIM <= float(matches.group(1)) <= HIGH_X_LIM
           and LOW_Y_LIM <= float(matches.group(2)) <= HIGH_Y_LIM):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
