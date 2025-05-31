# @leet start
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(
            char for pair in zip_longest(word1, word2, fillvalue="") for char in pair
        )


# @leet end
