# @leet start
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            if i == sum(map(int, str(num))):
                return i

        return -1


# @leet end
