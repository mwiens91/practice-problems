# @leet start
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        # Let dp[c] be the maximum sum we can achieve <= c using stones
        # up to the ith stone (where i is the below outer loop iteration
        # count)
        total = sum(stones)
        target = total // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for c in range(target, stone - 1, -1):
                dp[c] = max(dp[c], dp[c - stone] + stone)

        return total - 2 * dp[target]


# @leet end
