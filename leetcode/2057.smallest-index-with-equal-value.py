# @leet start
class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if num == i % 10:
                return i

        return -1


# @leet end
