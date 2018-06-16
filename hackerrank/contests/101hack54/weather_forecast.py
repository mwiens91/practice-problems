#!/usr/bin/env python3

import sys
import re


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
arrays = [[int(x) for x in re.split(r' ', line)] for line in lines]

# Print answer
print(sum([abs(x - y) for x, y in zip(arrays[0], arrays[1])]))
