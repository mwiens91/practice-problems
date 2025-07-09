# @leet start
from collections import Counter
import math


class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        # Count the total number of triplets, then remove triplets that
        # are not pairwise distinct
        n = len(nums)

        count = math.comb(n, 3)

        for freq in Counter(nums).values():
            if freq >= 2:
                count -= math.comb(freq, 2) * (n - freq)

            if freq >= 3:
                count -= math.comb(freq, 3)

        return count


# @leet end
