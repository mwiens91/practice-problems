#!/usr/bin/env python3

import itertools
import math
import sys

# All possible 3x3 magic squares
magic_squares = [
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
]

# Parse the current square from stdin
square = [[int(x) for x in line.split()] for line in sys.stdin]

# Find which magic square minimizes the cost
min_cost = math.inf

for ms in magic_squares:
    # Compute the cost
    cost = 0

    for row, col in itertools.product([0, 1, 2], [0, 1, 2]):
        cost += abs(ms[row][col] - square[row][col])

    # Update the minimum cost
    min_cost = min(min_cost, cost)

# Print the minimum cost
print(min_cost)
