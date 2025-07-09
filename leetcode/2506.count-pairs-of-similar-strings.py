# @leet start
from collections import Counter
import math


class Solution:
    def similarPairs(self, words: list[str]) -> int:
        # Define a function to convert characters present in a string to
        # a bitmask
        CODE_POINT_LOWER_A = ord("a")

        def make_bitmask_from_word(word: str) -> int:
            mask = 0

            for chr in word:
                mask |= 1 << (ord(chr) - CODE_POINT_LOWER_A)

            return mask

        # Count the number of words that share a given bitmask
        bitmask_counts = Counter(map(make_bitmask_from_word, words))

        return sum(math.comb(count, 2) for count in bitmask_counts.values())


# @leet end
