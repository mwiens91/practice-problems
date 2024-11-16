# @leet start
import math


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # NOTE: needed to use NeetCode to understand how to do solution

        # The idea here is to recognize that there is always a peak
        # number in the array because of the boundary conditions. I'm
        # too tired to be able to understand and articulate precisely
        # why that is. Maybe I'll come back to it when I'm more lucid.
        # (Probably definitely not.)
        n = len(nums)

        left = 0
        right = n - 1

        while True:
            mid = (left + right) // 2

            mid_num = nums[mid]
            mid_left_num = -math.inf if mid == 0 else nums[mid - 1]
            mid_right_num = -math.inf if mid == n - 1 else nums[mid + 1]

            if mid_left_num < mid_num and mid_right_num < mid_num:
                # Found peak element
                return mid

            if mid_left_num > mid_num:
                right = mid - 1
            else:
                # mid_right_num > mid_num
                left = mid + 1


# @leet end
