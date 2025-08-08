# @leet start
import itertools


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        return sum(1 for x, y in itertools.combinations(nums, 2) if x + y < target)


# @leet end
