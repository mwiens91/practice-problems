# @leet start
from collections import Counter
from string import ascii_lowercase


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counts = Counter(s)
        t_counts = Counter(t)

        result = 0

        for char in ascii_lowercase:
            result += max(0, s_counts[char] - t_counts[char])

        return result


# @leet end
