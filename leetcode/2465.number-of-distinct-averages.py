# @leet start
class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        # Sort the array
        nums.sort()

        # Use a forward and backward pointer, keeping track of the
        # averages of the two numbers the pointers point to
        left = 0
        right = len(nums) - 1

        averages: set[float] = set()

        while left < right:
            averages.add((nums[left] + nums[right]) / 2)

            left += 1
            right -= 1

        return len(averages)


# @leet end
