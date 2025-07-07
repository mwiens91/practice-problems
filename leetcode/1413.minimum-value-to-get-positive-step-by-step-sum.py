# @leet start
from itertools import accumulate


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        return max(1, 1 - min(accumulate(nums)))


# @leet end
