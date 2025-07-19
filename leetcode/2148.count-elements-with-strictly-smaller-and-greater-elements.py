# @leet start
class Solution:
    def countElements(self, nums: list[int]) -> int:
        nums_min = min(nums)
        nums_max = max(nums)

        return sum(1 for num in nums if nums_min < num < nums_max)


# @leet end
