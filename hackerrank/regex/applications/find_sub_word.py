#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
raw_lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
n = int(raw_lines[0])
lines = raw_lines[1:n+1]
queries = raw_lines[n+2:]

# Find all of the words in the lines
words = []
for line in lines:
    words += re.findall(r'(?<!\w)(\w+)(?!\w)', line)

# Go through each query and count how many times it appears as a subword
for query in queries:
    count = 0
    for word in words:
        count += len(re.findall(r'\w' + query + r'\w', word))

    # Print the result
    print(count)
