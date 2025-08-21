# @leet start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Let dp[j] be the number of distinct subsequences of t[:j] in
        # s[:i], where i is the iteration count of the below outer
        # loop
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for char in s:
            for j in range(n, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]


# @leet end
