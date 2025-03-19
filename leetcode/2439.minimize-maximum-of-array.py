# @leet start
from itertools import accumulate
import math


class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        # Go through each prefix and find the maximum average value,
        # rounded up: call this value x. For each prefix, the minimum
        # maximum value we can achieve is x. Since we can only add value
        # to each prefix and not remove it the minimum maximum value of
        # the entire list is the maximum of x.
        minimum_maximum_value = -math.inf

        for length, prefix_sum in enumerate(accumulate(nums), start=1):
            minimum_maximum_value = max(
                minimum_maximum_value, math.ceil(prefix_sum / length)
            )

        return minimum_maximum_value


# @leet end
