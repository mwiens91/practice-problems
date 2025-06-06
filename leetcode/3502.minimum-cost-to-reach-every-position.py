# @leet start
import itertools


class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        return list(itertools.accumulate(cost, func=min))


# @leet end
