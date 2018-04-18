#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Find the number of tweets
count = 0

for line in lines[1:]:
    count += len(re.findall(r'\b[@#]?hackerrank\b', line, re.IGNORECASE))

# Print the result
print(count)
