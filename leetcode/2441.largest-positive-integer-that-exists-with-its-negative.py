# @leet start
class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums_set = set(nums)

        return max((num for num in nums_set if -num in nums_set), default=-1)


# @leet end
