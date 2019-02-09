#!/usr/bin/env python3

from bisect import bisect_right
import sys
from typing import List


# Constants
INFEASIBLE = "no answer"


def next_lexicographical_permutation(l: List[int]) -> List[int]:
    """Get next lexicographical permutation.

    See
    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    for algorithm details. Returns the original string if this is this
    is the lexicographically largest permutation.
    """
    # Get longest non-decreasing suffix
    N = len(l)
    suffix = [l[-1]]

    for i in range(N - 2, -1, -1):
        if l[i] >= suffix[-1]:
            suffix.append(l[i])
        else:
            break

    suffix.reverse()

    # Return original list if it is the lexicographically greatest
    # permutation
    M = len(suffix)

    if M == N:
        return l

    # Move the pivot element into the suffix
    pivot = l[N - M - 1]
    swap_idx = M - 1 - bisect_right(list(reversed(suffix)), pivot)
    swap = suffix[swap_idx]
    suffix[swap_idx] = pivot

    return l[: N - M - 1] + [swap] + sorted(suffix)


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse test cases - translate each string to ordinal value (we'll go
# back the other way later)
cases = [[ord(i) for i in case] for case in lines[1:]]

# Solve each test case
for case in cases:
    # Find the next lexicographical permutation
    solution = next_lexicographical_permutation(case)

    # Convert ordinals back a string
    str_solution = "".join([chr(i) for i in solution])

    # Print solution
    if solution == case:
        print(INFEASIBLE)
    else:
        print(str_solution)
