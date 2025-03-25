# @leet start
import itertools


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return list(itertools.accumulate(nums))


# @leet end
