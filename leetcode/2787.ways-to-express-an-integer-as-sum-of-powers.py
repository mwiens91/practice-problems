# @leet start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD_VAL = 10**9 + 7

        # dp[c] is the number of ways we can express c as the sum of xth
        # powers of the first i positive integers (where i is the
        # iteration count of the below outer loop)
        dp = [0] * (n + 1)
        dp[0] = 1

        i = 1

        while (val := i**x) <= n:
            for c in range(n, val - 1, -1):
                dp[c] = (dp[c] + dp[c - val]) % MOD_VAL

            i += 1

        return dp[n]


# @leet end
