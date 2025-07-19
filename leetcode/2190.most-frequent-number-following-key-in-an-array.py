# @leet start
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        target_counts: defaultdict[int, int] = defaultdict(int)

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target_counts[nums[i + 1]] += 1

        return max(target_counts, key=target_counts.get)


# @leet end
