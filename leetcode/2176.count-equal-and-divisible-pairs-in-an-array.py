# @leet start
from collections import defaultdict
from itertools import combinations


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # Get indices for each number present in nums
        num_idxs: defaultdict[int, list[int]] = defaultdict(list)

        for i, num in enumerate(nums):
            num_idxs[num].append(i)

        # Get count of pairs satisfying condition
        pair_counts = 0

        for idx_list in num_idxs.values():
            for i, j in combinations(idx_list, 2):
                if i * j % k == 0:
                    pair_counts += 1

        return pair_counts


# @leet end
