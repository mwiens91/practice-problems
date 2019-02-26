#!/usr/bin/env python3

import itertools
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Set up grid
height, width = [int(x) for x in lines[0].split()]
grid = (
    [[0] * (width + 2)]
    + [[0] + [int(x) for x in line.split()] + [0] for line in lines[1:]]
    + [[0] * (width + 2)]
)

# Calculate surface area
area = 2 * height * width

for y, x in itertools.product(range(1, height + 1), range(1, width + 1)):
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        area += max(0, grid[y][x] - grid[y + dy][x + dx])

# Print surface area
print(area)
