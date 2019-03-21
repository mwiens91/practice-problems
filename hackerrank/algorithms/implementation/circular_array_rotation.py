#!/usr/bin/env python3

import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Parse input
n, k, _ = [int(i) for i in lines[0].split()]
l = [int(i) for i in lines[1].split()]
queries = [int(line) for line in lines[2:]]

# Solve each query
for q in queries:
    print(l[-((k - q) % n)])
