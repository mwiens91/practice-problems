# @leet start
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # Get a counter of the words that we have
        counts = Counter(words)

        # Put the words on the heap
        heap = []

        for word, count in counts.items():
            # This becomes a max heap with the words in sorted order if
            # we take the negative of the count
            tuple_ = (-count, word)

            # Push to heap
            heapq.heappush(heap, tuple_)

        # Return the k most frequent words in the right order
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


# @leet end
