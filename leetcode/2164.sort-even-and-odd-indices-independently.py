# @leet start
from itertools import zip_longest


class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        n = len(nums)

        return [
            val
            for pair in zip_longest(
                sorted(nums[i] for i in range(0, n, 2)),
                sorted((nums[i] for i in range(1, n, 2)), reverse=True),
            )
            for val in pair
            if val is not None
        ]


# @leet end
