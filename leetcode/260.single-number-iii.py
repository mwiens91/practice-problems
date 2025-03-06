# @leet start
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        return [num for num, count in Counter(nums).items() if count == 1]


# @leet end
