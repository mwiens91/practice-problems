# @leet start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        # This is an 0/1 knapsack variant. dp[c] tells us if we can form
        # the sum c using the first i elements of nums, where i is the
        # iteration count of the outer loop below.
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for c in range(target, num - 1, -1):
                dp[c] |= dp[c - num]

        return dp[target]


# @leet end
