# @leet start
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        n = len(nums)

        # Get product frequencies
        product_freqs: defaultdict[int, int] = defaultdict(int)

        for i in range(n):
            for j in range(i + 1, n):
                product_freqs[nums[i] * nums[j]] += 1

        # Find number of tuples
        count = 0

        for freq in product_freqs.values():
            # We can form n choose 2 pairs. For each pair there are 8
            # ways we can arrange the elements in the tuple.
            count += 4 * freq * (freq - 1)

        return count


# @leet end
