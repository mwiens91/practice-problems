# @leet start
from collections import Counter


class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)

        num_pairs = 0

        for count in counts.values():
            num_pairs += count // 2

        return [num_pairs, len(nums) - num_pairs * 2]


# @leet end
