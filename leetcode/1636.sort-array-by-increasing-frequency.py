# @leet start
from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)

        return sorted(nums, key=lambda x: (counts[x], -x))


# @leet end
