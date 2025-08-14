# @leet start
class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # dp[i][j] is the largest number of strings that can be used in
        # a subset containing a total of i <= m 0s and j >= n 1s using
        # the first k (the iteration count of the outer loop below)
        # elements of strs
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str_ in strs:
            num_zeros = 0
            num_ones = 0

            for char in str_:
                if char == "0":
                    num_zeros += 1
                else:
                    num_ones += 1

            for i in range(m, num_zeros - 1, -1):
                for j in range(n, num_ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - num_zeros][j - num_ones] + 1)

        return dp[m][n]


# @leet end
