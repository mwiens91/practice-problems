# @leet start
from itertools import zip_longest
from operator import itemgetter


class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        return all(c1 == c2 for c1, c2 in zip_longest(s, map(itemgetter(0), words)))


# @leet end
