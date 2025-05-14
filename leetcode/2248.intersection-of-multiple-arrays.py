# @leet start
from functools import reduce


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        return sorted(
            reduce(lambda accum, s: accum.intersection(s), (set(l) for l in nums))
        )


# @leet end
