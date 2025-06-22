# @leet start
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        return sum(
            1
            for i in range(1, len(nums) - 1)
            if nums[i - 1] + nums[i + 1] == nums[i] / 2
        )


# @leet end
