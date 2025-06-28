# @leet start
import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        # We need to find an integer x such that
        #
        # \sum_{i = 1}^x i == \sum{i = x}^n i
        #
        # Doing some math, we can solve for x:
        #
        # x = sqrt(n * (n + 1) / 2)
        x_squared = n * (n + 1) // 2
        x = math.isqrt(x_squared)

        return x if x * x == x_squared else -1


# @leet end
