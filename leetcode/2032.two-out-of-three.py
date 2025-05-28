# @leet start
from collections import Counter
import itertools


class Solution:
    def twoOutOfThree(
        self, nums1: list[int], nums2: list[int], nums3: list[int]
    ) -> list[int]:
        # Get the distinct elements of each list, combine them into a
        # single list, and then count the frequency of each element
        counts = Counter(itertools.chain.from_iterable(map(set, [nums1, nums2, nums3])))

        # Find elements that occur in at least two of the lists
        results: list[int] = []

        for val, count in counts.items():
            if count >= 2:
                results.append(val)

        return results


# @leet end
