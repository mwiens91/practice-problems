# @leet start
from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        return all(count <= 2 for count in Counter(nums).values())


# @leet end
