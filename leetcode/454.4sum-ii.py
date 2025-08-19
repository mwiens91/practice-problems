# @leet start
from collections import defaultdict
import itertools


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]
    ) -> int:
        n = len(nums1)

        # Find sums we can make by combining nums from nums1 and
        # nums2; and nums 3 and nums 4
        sum_freqs_12: defaultdict[int, int] = defaultdict(int)
        sum_freqs_34: defaultdict[int, int] = defaultdict(int)

        for i, j in itertools.product(range(n), range(n)):
            sum_freqs_12[nums1[i] + nums2[j]] += 1
            sum_freqs_34[nums3[i] + nums4[j]] += 1

        # Find the number of zero sums
        zero_sums = 0

        for partial_sum in sum_freqs_12:
            if -partial_sum in sum_freqs_34:
                zero_sums += sum_freqs_12[partial_sum] * sum_freqs_34[-partial_sum]

        return zero_sums


# @leet end
