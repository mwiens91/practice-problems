# @leet start
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s).values()

        even_freqs: list[int] = []
        odd_freqs: list[int] = []

        for freq in freqs:
            if freq % 2 == 0:
                even_freqs.append(freq)
            else:
                odd_freqs.append(freq)

        return max(odd_freqs) - min(even_freqs)


# @leet end
