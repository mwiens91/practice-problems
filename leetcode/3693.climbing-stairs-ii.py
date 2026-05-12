# @leet start
class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [0] + costs

        for i in range(1, n + 1):
            dp[i] += min(dp[j] + (j - i) ** 2 for j in range(i - 3, i))

        return dp[n]


# @leet end
