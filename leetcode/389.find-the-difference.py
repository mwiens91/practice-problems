# @leet start
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counts = Counter(s)
        t_counts = Counter(t)

        for char, t_count in t_counts.items():
            if char not in s_counts or t_count > s_counts[char]:
                return char


# @leet end
