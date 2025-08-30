# @leet start
import math


class Solution:
    def minSteps(self, n: int) -> int:
        def find_smallest_factor_gt_one(num: int) -> int:
            for i in range(2, math.isqrt(num) + 1):
                if num % i == 0:
                    return i

            return num

        # Treat this as one-indexed for convenience, and ignore
        # the 0-index value
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            smallest_factor = find_smallest_factor_gt_one(i)

            if smallest_factor < i:
                # Copy the largest factor < i and paste it
                # smallest_factor - 1 times
                dp[i] = dp[i // smallest_factor] +  smallest_factor
            else:
                # i is prime, we need to copy and paste i - 1 times
                dp[i] = i

        return dp[n]


# @leet end
