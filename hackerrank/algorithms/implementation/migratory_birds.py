#!/usr/bin/env python3

from collections import Counter
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
nums = sorted([int(x) for x in lines[1].split()])

# Grab most common element, choosing the last element if there are ties
counts = Counter(nums)
print(counts.most_common(1)[0][0])
