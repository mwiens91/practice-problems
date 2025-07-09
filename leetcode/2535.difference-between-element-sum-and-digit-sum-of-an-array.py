# @leet start
from itertools import chain


class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        return abs(
            sum(nums) - sum(chain.from_iterable(map(int, str(num)) for num in nums))
        )


# @leet end
