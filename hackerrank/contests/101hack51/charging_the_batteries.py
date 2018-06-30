#!/usr/bin/env python3

import math
import re
import sys


def transform_coordinate_to_value(x, y):
    global wall_length

    if x and not y:
        # Bottom edge
        return x
    elif x == wall_length:
        # Right edge
        return wall_length + y
    elif y == wall_length:
        # Top edge
        return wall_length * 3 - x
    elif y and not x:
        # Left edge
        return wall_length * 4 - y
    else:
        # Origin
        return 0


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
wall_length, num_sockets, num_controllers = (
    [int(x) for x in re.split(r'\D', lines[0])])
socket_coords = [[int(x) for x in re.split(r'\D', line)] for line in lines[1:]]

# Assign a distance value to each socket
socket_vals = [transform_coordinate_to_value(*coord)
               for coord in socket_coords]

# Sort the values
socket_vals.sort()

# Now find the minimum distance to num_controllers consecutive sockets
minimum_distance = math.inf

for i in range(num_sockets):
    index_to_add = i + num_controllers - 1

    if index_to_add >= num_sockets:
        index_to_add -= num_sockets
        additional_loop = 4 * wall_length
    else:
        additional_loop = 0

    # Update the minimum distance
    minimum_distance = min(
        minimum_distance,
        socket_vals[index_to_add] + additional_loop - socket_vals[i])

# Print the answer
print(minimum_distance)
