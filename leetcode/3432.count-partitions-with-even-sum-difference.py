# @leet start
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0


# @leet end
