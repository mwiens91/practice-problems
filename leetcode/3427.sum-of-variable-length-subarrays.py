# @leet start
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        prefix_sums = list(accumulate(nums))

        result = 0

        for i, num in enumerate(nums):
            result += prefix_sums[i]

            if (start := i - num) > 0:
                result -= prefix_sums[start - 1]

        return result


# @leet end
