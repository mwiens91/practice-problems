#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse test cases
test_cases = []
i = 1

while i < len(lines):
    # Read in this test case
    n = int(lines[i])

    test_cases += [
        [[int(i) for i in line.split()] for line in lines[i + 1 : i + n + 1]]
    ]

    # Set up for next iteration
    i += n + 1

for test_case in test_cases:
    # Make sure we can fit all balls of each type into a container
    row_sums = [sum(r) for r in test_case]
    col_sums = [sum(c) for c in zip(*test_case)]

    if sorted(row_sums) == sorted(col_sums):
        print("Possible")
    else:
        print("Impossible")
