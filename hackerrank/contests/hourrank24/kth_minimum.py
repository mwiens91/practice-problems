#!/usr/bin/env python3

import re
import sys


def insert_into_smallest(element, remove_first=False):
    """Insert a new element into list of smallest elements."""
    global smallest, smallest_length, k

    # Remove the largest element if required
    if remove_first:
        if k == 1:
            # Deal with trivial case
            smallest = [element]
            return

        smallest = smallest[1:]
        smallest_length -= 1

    # Insert the new element
    start = 0
    end = smallest_length - 1
    testidx = 0

    # Do a binary search/insertion
    while True:
        testidx = (start + end) // 2

        if testidx < 0:
            # Protect against negative floors
            testidx = 0

        if start >= end:
            break

        if element == smallest[testidx]:
            break
        elif element > smallest[testidx]:
            end = testidx - 1
        else:
            start = testidx + 1

    if element < smallest[testidx]:
        testidx += 1

    smallest = smallest[:testidx] + [element] + smallest[testidx:]
    smallest_length += 1

# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Parse input
n, m, x, k = [int(i) for i in re.split(r'\D', lines[0])]
A = [int(i) for i in re.split(r' ', lines[1])]
B = [int(i) for i in re.split(r' ', lines[2])]

# List to hold the k smallest elements
smallest = [0]
smallest_length = 0

# Look at the elements in the generated list, and keep the kth largest
# numbers
for i in range(min(n, m - x)):
    for j in range(i + x, m):
        # Find the element
        this_element = A[i] * B[j]

        if smallest_length < k:
            # Build up the list
            if not smallest_length:
                # Deal with first element
                smallest[0] = this_element
                smallest_length += 1
            else:
                insert_into_smallest(this_element)
        elif this_element < smallest[0]:
            insert_into_smallest(this_element, remove_first=True)

# Print the answer
print(smallest[0])
