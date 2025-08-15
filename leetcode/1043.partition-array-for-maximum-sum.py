# @leet start
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        # dp[i] is the maximum sum we can achieve starting at
        # the index i
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            partition_max = 0

            for l in range(1, min(k, n - i) + 1):
                partition_max = max(partition_max, arr[i + l - 1])
                dp[i] = max(dp[i], partition_max * l + dp[i + l])

        return dp[0]


# @leet end
