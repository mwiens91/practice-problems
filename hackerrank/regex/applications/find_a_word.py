#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse the input
n = int(lines[0])
sentences = lines[1:n+1]
queries = lines[n+2:]

# Find all of the words
words = []

for sentence in sentences:
    words += re.findall(r'(?<!\w)(\w+)(?!\w)', sentence)

# Now count the occurances of each query
for query in queries:
    print(words.count(query))
