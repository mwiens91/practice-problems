#!/usr/bin/env python3

import math
import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
test_cases = [[int(i) for i in re.split('\D', line)] for line in lines[1:]]

# Solve each test case
for test in test_cases:
    # Get the problem variables
    a, b, x = test

    # Check if possible
    if b - a + 1 < x:
        print(-1)

    # Print solution
    b_half = math.ceil(b/2)

    if x <= b_half:
        print(*range(b, b - x, -1))
    else:
        print(-1)
