# @leet start
from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)

        return sum(counts[num + k] for num in nums)


# @leet end
