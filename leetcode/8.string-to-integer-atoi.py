# @leet start
class Solution:
    def myAtoi(self, s: str) -> int:
        # Handle edge case of s == ""
        if s == "":
            return 0

        # Implement the steps as instructed
        n = len(s)

        i = 0

        # Step 1: whitespace
        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        # Step 2: signedness
        negative = False

        if s[i] in {"-", "+"}:
            if s[i] == "-":
                negative = True

            i += 1

        if i == n:
            return 0

        # Step 3: conversion
        start_i = i

        while i < n and s[i] in {str(x) for x in range(10)}:
            i += 1

        # No valid digits
        if start_i == i:
            return 0

        # Valid digits
        result = int(s[start_i:i])

        if negative:
            result *= -1

        # Step 4: rounding
        if result < -(2**31):
            result = -(2**31)
        elif result > 2**31 - 1:
            result = 2**31 - 1

        return result


# @leet end
