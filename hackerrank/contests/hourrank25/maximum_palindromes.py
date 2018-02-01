#!/usr/bin/env python3

import re
import sys


def find_num_palindromes(i, j):
    """Counts palindromes.

    Finds the number of palindromes inside substring marked by i, j.
    """
    # Explicitly using the outside counts list
    global counts

    # Count letters in the substring
    if not i:
        count = counts[j]
    else:
        count = [b - a for a, b in zip(counts[i - 1], counts[j])]

    # Count number of even pairs of letters. Abort if there is more than
    # one odd number of a letter
    pairs = 0
    odds = 0
    for lettercount in count:
        if lettercount % 2:
            odds += 1

            # Abort if more than one odd number of a letter
            if odds == 2:
                return 0
        else:
            pairs += lettercount / 2

    return pairs


# Read lines from stdin
lines = [line.strip() for line in sys.stdin.readlines()]

# Get relevant variables - note that unlike in the problem description,
# here l and r are zero-indexed
s = lines[0]
length = len(s)
testindices = [[int(x) - 1 for x in re.split(r"\D", line)]
                                            for line in lines[2:]]

# Prepare a list that contains count of letters up to index i of s
# (inclusive)
counts = [[0]*26]

# Fill up the counts list
for idx, letter in enumerate(s):
    # Copy previous counts if it's not the first time through
    if idx:
        counts.append(counts[idx - 1][:])

    # Increase the count
    counts[idx][ord(letter) - ord('a')] += 1

# Now go through substrings
for l, r in testindices:
    find_num_palindromes(l,r)
