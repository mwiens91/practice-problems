# @leet start
from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counter_intersection = reduce(
            lambda c_intersect, c: c_intersect & c, (Counter(word) for word in words)
        )

        common_chars = []

        for char, count in counter_intersection.items():
            common_chars += [char] * count

        return common_chars


# @leet end
