# @leet start
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Get a count of each num in nums and grab the k most common.
        # most_common uses heaps and its complexity is O(n log k).
        return [n[0] for n in Counter(nums).most_common(k)]


# @leet end
