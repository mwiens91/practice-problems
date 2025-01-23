# @leet start
class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max_distance = 0

        for i, num in enumerate(nums):
            prev_num = nums[i - 1]  # when i = 0, this is the final element of nums
            max_distance = max(max_distance, abs(num - prev_num))

        return max_distance


# @leet end
