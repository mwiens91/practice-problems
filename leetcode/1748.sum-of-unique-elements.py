# @leet start
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)

        sum_ = 0

        for num, count in counts.items():
            if count == 1:
                sum_ += num

        return sum_


# @leet end
