# @leet start
from itertools import accumulate
import random


class Solution:

    def __init__(self, w: list[int]):
        self.prefix_sums = list(accumulate(w))

        self.n = len(self.prefix_sums)
        self.total_weight = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        """Pick an index given its weighted probability.

        First we pick a random number between 1 and the total weight.
        Then we find the insertion point index of this number in the
        prefix sums list.

        This is equivalent picking an index given its weighted
        probability because each prefix sum represents a range between
        the last prefix sum (exclusive) and itself (inclusive) with
        width directly proportional to its weight. The random number
        falls into one of these ranges, and it will fall into any given
        range with probability equal to the width of the range.
        """
        # Get a random number between 1 and the total weight
        random_num = random.randint(1, self.total_weight)

        # Perform a binary search to find the insertion point of this
        # number in the prefix sums list
        left = 0
        right = self.n - 1

        while left <= right:
            mid = (left + right) // 2

            if self.prefix_sums[mid] >= random_num:
                right = mid - 1
            else:
                left = mid + 1

        # Return the insertion point index
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @leet end
