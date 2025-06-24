# @leet start
from collections import Counter
from string import ascii_lowercase


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counts1 = Counter(word1)
        counts2 = Counter(word2)

        return all(abs(counts1[char] - counts2[char]) <= 3 for char in ascii_lowercase)


# @leet end
