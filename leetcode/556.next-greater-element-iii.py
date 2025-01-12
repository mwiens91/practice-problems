# @leet start
import math


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Translation: find the next permutation. Get the numbers in n
        # first.
        nums = [int(c) for c in str(n)]

        # We find the "pivot index", which is the greatest index i such
        # that nums[i] < nums[i + 1], by moving from the back of the
        # array to the front
        n = len(nums)

        pivot_idx = None

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                # Found the pivot index
                pivot_idx = i - 1

                break

        # Get out if there is no pivot index
        if pivot_idx is None:
            return -1

        # From the pivot index forward, swap the pivot with the smallest
        # element greater than the pivot with the largest possible index
        # (in the case that this smallest element is repeated). The
        # first step is to find the the element to swap the pivot with.
        pivot_num = nums[pivot_idx]
        to_swap_num = math.inf

        for i in range(pivot_idx + 1, n):
            current_num = nums[i]

            # Since everything after the pivot is in descending order,
            # we can stop our search once we hit numbers that are equal
            # to or smaller than the pivot
            if pivot_num >= current_num:
                break

            if current_num <= to_swap_num:
                to_swap_num = current_num
                to_swap_idx = i

        # Do the swap
        nums[pivot_idx], nums[to_swap_idx] = nums[to_swap_idx], nums[pivot_idx]

        # We finish by reversing all numbers after the pivot index
        left = pivot_idx + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

        # Return the result
        next_greater_element = int("".join(str(x) for x in nums))

        if next_greater_element > 2**31 - 1:
            return -1

        return next_greater_element


# @leet end
