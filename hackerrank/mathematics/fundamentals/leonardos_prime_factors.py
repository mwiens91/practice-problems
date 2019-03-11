#!/usr/bin/env python3

import sys

# All prime numbers (plus a few) we need given the problem constraints
PRIME_NUMBERS = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
]


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
queries = [int(i) for i in lines[1:]]

# Solve each query
for query in queries:
    prod = 1
    count = 0

    for prime in PRIME_NUMBERS:
        prod *= prime

        if prod > query:
            break

        count += 1

    print(count)
