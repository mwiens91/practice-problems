# @leet start
import itertools


class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD_VAL = int(1e9 + 7)

        # Find the minimum number of exponents i such that
        # sum(2^i) = n
        exponents: list[int] = []
        i = 0

        while n:
            if n & 1:
                exponents.append(i)

            i += 1
            n >>= 1

        # Get the prefix sum of exponents
        prefix_sums = list(itertools.accumulate(exponents, initial=0))

        # Return query answers
        return [
            (1 << (prefix_sums[end + 1] - prefix_sums[start])) % MOD_VAL
            for start, end in queries
        ]


# @leet end
