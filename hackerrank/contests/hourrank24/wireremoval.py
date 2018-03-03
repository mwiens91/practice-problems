#!/usr/bin/env python3

import copy
import re
import resource
import sys


# Recurse forever
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)

def depth_first_search(node, depth):
    """Recursive function to do depth first search."""
    global adjacency, visited, weighted_sizes, distance_sum

    # Mark this as a visited node
    visited[node] = True

    # Size of subtree
    size = 1

    # Visit each child
    for child in adjacency[node]:
        if not visited[child]:
            size += depth_first_search(child, depth + 1)

    # Compute weighted sizes and distance sum
    weighted_sizes += depth * size
    distance_sum += depth

    return size

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
num_vertices = int(lines[0])
edges = [[int(x) - 1 for x in re.split(r'\D', line)] for line in lines[1:]]

# Useful lists
adjacency = [[] for i in range(num_vertices)]
visited = [False for i in range(num_vertices)]

# Variables we'll sum to
weighted_sizes = 0
distance_sum = 0

# Build the adjacency list
for edge in edges:
    x, y = edge
    adjacency[x] += [y]
    adjacency[y] += [x]

# Do a depth first search
depth_first_search(0, 0)

# Give the result
expected_loss = weighted_sizes / distance_sum
print(num_vertices - expected_loss)
