# @leet start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(1 for num in nums if num < k)


# @leet end
