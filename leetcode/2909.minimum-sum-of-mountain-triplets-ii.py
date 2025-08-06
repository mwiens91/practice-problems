# @leet start
from itertools import accumulate
import math


class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        prefix_mins = list(accumulate(nums, func=min))
        suffix_mins = list(accumulate(reversed(nums), func=min))[::-1]

        min_mountain_sum = math.inf

        for i in range(1, len(nums) - 1):
            if nums[i] > prefix_mins[i - 1] and nums[i] > suffix_mins[i + 1]:
                min_mountain_sum = min(
                    min_mountain_sum, prefix_mins[i - 1] + nums[i] + suffix_mins[i + 1]
                )

        return min_mountain_sum if min_mountain_sum < math.inf else -1


# @leet end
