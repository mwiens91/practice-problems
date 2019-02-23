#!/usr/bin/env python3

from functools import reduce
from math import ceil, floor, sqrt
import sys


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Put all of the input into one big string
msg = reduce(lambda msg, s: msg + s.replace(" ", ""), lines)

# Frame the message into an m x n matrix
msg_len = len(msg)
msg_side_len = sqrt(msg_len)
m = floor(msg_side_len)
n = ceil(msg_side_len)

# Ensure the message fits in the matrix (note: there's probably a more
# concise way of doing this)
while m * n < msg_len:
    m += 1

# Form the encrypted string
encrypted_msg = ""

for j in range(n):
    for i in range(m):
        try:
            encrypted_msg += msg[i * n + j]
        except IndexError:
            pass

    encrypted_msg += " "

# Print the answer
print(encrypted_msg)
