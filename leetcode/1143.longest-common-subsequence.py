# @leet start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        # dp[j] represents the longest common subsequence between
        # text1[:i] and text2[:j] where i is the iteration count of the
        # below outer loop
        dp = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            # Because we need access to dp[j - 1] for i - 1 we'll put
            # this in a temp variable, which saves us from using a 2D DP
            # array
            prev_diag = 0

            for j in range(1, n2 + 1):
                temp = dp[j]

                dp[j] = (
                    prev_diag + 1
                    if text1[i - 1] == text2[j - 1]
                    else max(dp[j], dp[j - 1])
                )

                prev_diag = temp

        return dp[n2]


# @leet end
