#!/usr/bin/env python3

from math import (
    ceil,
    cos,
    radians,
    sin,
)
import sys
import numpy as np


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse the input
radius = int(lines[0])
angles_per_letter = [float(line.split()[1]) for line in lines[1:27]]

raw_codeword = lines[27]

# Clean up the codeword
codeword = ""

for lett in raw_codeword:
    upper_lett = lett.upper()

    if upper_lett.isalpha() and not codeword.endswith(upper_lett):
        codeword += upper_lett

codeword = [ord(l) - ord('A') for l in codeword]

# Precompute distances between letters
distances = np.zeros((26, 26))

for i in range(26):
    # Get angle for point of interest
    theta = radians(angles_per_letter[i])

    # Form the point of interest
    x = np.array((cos(theta), sin(theta)))

    for j in range(i + 1, 26):
        # Get angle for other point of interest
        phi = radians(angles_per_letter[j])

        # Form the points
        y = np.array((cos(phi), sin(phi)))

        distances[i, j] = radius * np.linalg.norm(y - x)

# Reflect about diagonal
distances = distances + distances.transpose()

# Now solve the length of string needed to form codeword
final_sum = 0

for i in range(len(codeword) - 1):
    final_sum += distances[codeword[i], codeword[i + 1]]

# Give final answer
print(ceil(final_sum) + radius)
