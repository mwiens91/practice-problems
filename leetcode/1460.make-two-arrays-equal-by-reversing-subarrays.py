# @leet start
from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)


# @leet end
