# @leet start
class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        # Sort, then swap each pair of elements
        nums.sort()

        i = 0
        n = len(nums)

        while i < n:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

            i += 2

        return nums


# @leet end
