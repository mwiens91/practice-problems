#!/usr/bin/env python3

import math
import re
import sys


def find_num_max_palindromes(i, j):
    """Counts number of max length palindromes mod M.

    Finds the number of maximum length palindromes inside substring
    marked by i, j mod M.
    """
    # Explicitly using the outside counts list and the divisor M
    global counts, M

    # Deal with the explicit trivial cases here
    if j - i <= 1:
        return 1

    # Count letters in the substring
    if not i:
        count = counts[j]
    else:
        count = [b - a for a, b in zip(counts[i - 1], counts[j])]

    # Count number of even pairs of letters. And the number of duplicate
    # pairs for each letter if there are any.
    pairs = 0
    odds = 0
    duplicate_list = []
    for lettercount in count:
        # Check if there are an odd number a letter
        if lettercount % 2:
            odds += 1

        numpairs = lettercount // 2

        # Add duplicate pairs if needed
        if numpairs > 1:
            duplicate_list.append(numpairs)

        # Add the number of pairs to the total sum
        pairs += numpairs


    # This is using a (possibly well known?) discrete math formula
    # First calculate the factorial mod M of the pairs
    ans = 1
    for k in range(1, pairs+1):
        ans = ans * k % M

    # Now divide by the factorial of each duplicate using fancy math
    for duplicate in duplicate_list:
        ans = ans * pow(math.factorial(duplicate), M-2, M) % M

    # Multiply by the number of odd numbers - 1 if there are any odd
    # numbers
    if not odds:
        pass
    else:
        ans = ans * odds % M

    return ans


# Set the divisor to mod our answers with
M = int(1e9) + 7

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
    print(find_num_max_palindromes(l, r))
