#!/usr/bin/env python3

import re
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_vertices = int(lines[0])
edges = [[int(x) for x in re.split(r'\D', line)] for line in lines[1:]]

# Create a list to weight the vertices
weights = [1] * num_vertices

# And another list to store the depth of each vertex
depths = [0] * num_vertices

# Go through the edges from edges including the highest vertex to the
# lowest
for edge in sorted(edges, key=lambda x: max(x), reverse=True):
    # Find the min and max vertices
    min_vert = min(edge)
    max_vert = max(edge)

    # Compute the weights
    weights[min_vert - 1] += weights[max_vert - 1]

# Go through the edges from edges including the lowest vertex to the
# highest
for edge in sorted(edges, key=lambda x: max(x)):
    # Find the min and max vertices
    min_vert = min(edge)
    max_vert = max(edge)

    # Compute the depths
    depths[max_vert - 1] = depths[min_vert - 1] + 1

# Find the expected value
sum_of_depths = sum(depths[1:])
probabilities = [d / sum_of_depths for d in depths]

weighted_losses = [probabilities[i] * weights[i] for i in range(num_vertices)]
weighted_loss = sum(weighted_losses)

print(weights)
print(depths)

print(num_vertices - weighted_loss)
