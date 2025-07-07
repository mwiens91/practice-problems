# @leet start
import math


class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        min_diff = math.inf

        for i in range(0, len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff


# @leet end
