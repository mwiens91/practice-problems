# @leet start
from collections import defaultdict


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        n = len(words)

        # Get the total character count of all words
        counts: defaultdict[str, int] = defaultdict(int)

        for word in words:
            for char in word:
                counts[char] += 1

        return all(count % n == 0 for count in counts.values())


# @leet end
