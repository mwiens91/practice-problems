# @leet start
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count_vals = Counter(arr).values()

        return len(count_vals) == len(set(count_vals))


# @leet end
