# @leet start
from itertools import accumulate


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        prefix_sums = list(accumulate(nums))
        suffix_sums = list(accumulate(nums[::-1]))[::-1]

        n = len(nums)

        for i in range(n):
            prefix_sum = prefix_sums[i - 1] if i > 0 else 0
            suffix_sum = suffix_sums[i + 1] if i < n - 1 else 0

            if prefix_sum == suffix_sum:
                return i

        return -1


# @leet end
