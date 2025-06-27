# @leet start
import heapq
import math


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        return math.prod(heapq.nlargest(2, nums)) - math.prod(heapq.nsmallest(2, nums))


# @leet end
