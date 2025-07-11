# @leet start
from itertools import combinations_with_replacement


class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        distinct_nums = set(nums)
        max_xor = 0

        for x, y in combinations_with_replacement(distinct_nums, 2):
            if abs(x - y) <= min(x, y):
                max_xor = max(max_xor, x ^ y)

        return max_xor


# @leet end
