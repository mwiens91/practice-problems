# @leet start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return min(1, len(set(nums)) - 1)


# @leet end
