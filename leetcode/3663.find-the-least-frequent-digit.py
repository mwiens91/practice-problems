# @leet start
from collections import defaultdict


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freqs: defaultdict[int, int] = defaultdict(int)

        while n:
            n, digit = divmod(n, 10)
            freqs[digit] += 1

        return min(freqs, key=lambda d: (freqs[d], d))


# @leet end
