# @leet start
from collections import Counter


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        # Despite the problem stating k >= 0, apparently there is a test
        # case which has k < 0, so we deal with that here (unfortunate)
        if k < 0:
            return 0

        # This is an O(n) time and memory solution. First get a counter
        # for the numbers in the input
        counter = Counter(nums)

        # Now determine the number of unique pairs. For each unique
        # number n1 in nums (i.e., each key in counter), we look for (if
        # k > 0) another unique number n2 in nums such that n2 = n1 + k
        # (or we could do n1 - k; we just need to choose one so we don't
        # double count); (if k == 0) whether there are at least two
        # occurances of n1.
        num_unique_pairs = 0

        for unique_num in counter:
            if k == 0:
                if counter[unique_num] >= 2:
                    num_unique_pairs += 1
            else:
                if unique_num + k in counter:
                    num_unique_pairs += 1

        return num_unique_pairs


# @leet end
