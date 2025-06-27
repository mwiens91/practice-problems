# @leet start
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freqs = Counter(nums).values()
        max_freq = max(freqs)

        return sum(freq for freq in freqs if freq == max_freq)


# @leet end
