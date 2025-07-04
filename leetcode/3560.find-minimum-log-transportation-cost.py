# @leet start
class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        # Either
        #
        # - n > k and m <= k
        # - m > k and n <= k
        # - n <= k and m <= k
        #
        # In the case where one of n or m is greater than k, the cost is
        # minimized by having the cut as unevenly distributed as
        # possible (easy to prove with basic calculus).
        if n > k:
            return k * (n - k)

        if m > k:
            return k * (m - k)

        return 0


# @leet end
