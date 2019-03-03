#!/usr/bin/env python3

from math import floor
import sys

# Constants
SUCCESS = "YES"
FAILURE = "NO"


# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Solve each test case
for test_case in lines[1:]:
    l = len(test_case)

    # Make sure special cases fail
    if test_case.startswith("0") or l == 1:
        print(FAILURE)

        continue

    # Iterate through all possible "beautiful" strings
    is_beautiful = False

    for i in range(1, floor(l / 2) + 1):
        # Build up the target string and look for a match
        head_str = test_case[:i]
        head_num = int(head_str)

        target_str = ""

        current_num = head_num + 1
        current_str = str(current_num)
        remaining_len = l - i

        while remaining_len >= len(current_str):
            target_str += current_str

            remaining_len -= len(current_str)
            current_num += 1
            current_str = str(current_num)

        if target_str == test_case[i:]:
            is_beautiful = True

            break

    # Print the results
    if is_beautiful:
        print(SUCCESS, head_str)
    else:
        print(FAILURE)
