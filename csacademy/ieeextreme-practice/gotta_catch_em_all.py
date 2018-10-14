#!/usr/bin/env python3

import sys
import numpy as np


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
r, c = [int(x) for x in lines[0].split()]
weights = np.matrix([[int(x) for x in line.split()] for line in lines[1:]])

# Set up the distances matrix
results = np.zeros((r, c), dtype=int)

results[r - 1, c - 1] = 1   # we need at least one health

for col in range(c - 2, -1, -1):
    results[r - 1, col] = max(
        results[r - 1, col + 1] - weights[r - 1, col],
        1,
    )

for row in range(r - 2, -1, -1):
    results[row, c - 1] = max(
        results[row + 1, c - 1] - weights[row, c - 1],
        1,
    )

# Now go through each middle element and pick the one that requires the
# least amount of health
for col in range(c - 2, -1, -1):
    for row in range(r - 2, -1, -1):
        minimum_next_step = min(
            results[row + 1, col],
            results[row, col + 1],
        )
        results[row, col] = max(
            minimum_next_step - weights[row, col],
            1,
        )

# Print the answer
print(results[0, 0])
