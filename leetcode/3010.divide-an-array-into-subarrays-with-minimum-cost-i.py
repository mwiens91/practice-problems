# @leet start
import heapq


class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        return nums[0] + sum(heapq.nsmallest(2, nums[1:]))


# @leet end
