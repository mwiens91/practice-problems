# @leet start
import heapq
from operator import itemgetter


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        # Put tuples (val, idx) in a heap, get the k largest elements,
        # sort them based on index, and return only the k largest
        # elements in a list in order of their indices
        return list(
            map(
                itemgetter(0),
                sorted(
                    heapq.nlargest(k, ((val, idx) for idx, val in enumerate(nums))),
                    key=itemgetter(1),
                ),
            )
        )


# @leet end
