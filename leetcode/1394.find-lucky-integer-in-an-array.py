# @leet start
from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        # Might be faster to keep track of a maximum and not do
        # sorting
        for num, count in sorted(Counter(arr).items(), reverse=True):
            if num == count:
                return num

        return -1


# @leet end
