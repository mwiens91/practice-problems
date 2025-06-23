# @leet start
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        return k * max(nums) + k * (k - 1) // 2


# @leet end
