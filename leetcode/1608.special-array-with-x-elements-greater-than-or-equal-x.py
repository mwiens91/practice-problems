# @leet start
from collections import Counter
import math


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        # We're told that if the array is special, then there is a
        # unique element x such that there are x numbers in the array
        # >= x. First get the counts of each number.
        counts = Counter(nums)

        # Then, go through each number x from the array and its
        # frequency in sorted order. Let the previous number processed
        # be x_prev. Then all numbers (not just numbers in the original
        # array) y such that x_prev < y <= x have the same number of
        # array elements greater than or equal to it. For each number x,
        # we see if the current number of array elements greater than or
        # equal to it exists in this range: if it does, we return that
        # the current number of array elements greater than or equal to
        # x.
        nums_greater_than_or_equal = len(nums)
        prev_num = -math.inf

        for num, freq in sorted(counts.items()):
            if prev_num < nums_greater_than_or_equal <= num:
                return nums_greater_than_or_equal

            # Set up for next number
            nums_greater_than_or_equal -= freq
            prev_num = num

        return -1


# @leet end
