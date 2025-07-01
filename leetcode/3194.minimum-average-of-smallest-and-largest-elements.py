# @leet start
import math


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1

        min_avg = math.inf

        while left < right:
            min_avg = min(min_avg, (nums[left] + nums[right]) / 2)

            left += 1
            right -= 1

        return min_avg


# @leet end
