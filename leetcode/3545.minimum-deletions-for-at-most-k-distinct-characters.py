# @leet start
from collections import Counter
import heapq


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # Put frequencies into a heap. While we are above the maximum
        # number of distinct numbers k, we pop character frequencies
        # from the heap.
        heap = list(Counter(s).values())
        heapq.heapify(heap)

        num_distinct = len(heap)
        deletions_required = 0

        while num_distinct > k:
            deletions_required += heapq.heappop(heap)
            num_distinct -= 1

        return deletions_required


# @leet end
