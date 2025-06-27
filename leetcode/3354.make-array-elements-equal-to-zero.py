# @leet start
from itertools import accumulate


class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        # Find for each index where a zero occurs. Add to the count once
        # if the sum of numbers on either side of that index differ by
        # exactly 1. Add to the count twice if the sum of numbers is
        # equal.
        prefix_sums = list(accumulate(nums))
        total_sum = prefix_sums[-1]

        count = 0

        for num, left_sum in zip(nums, prefix_sums):
            if num == 0:
                abs_diff = abs(2 * left_sum - total_sum)

                if abs_diff == 0:
                    count += 2
                elif abs_diff == 1:
                    count += 1

        return count


# @leet end
