# @leet start
from collections import defaultdict
from math import comb


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # First, for each domino, count the number of equivalent dominos
        # where the keys to the counter dictionary are the domino values
        # in sorted order
        counts: defaultdict[tuple[int, int], int] = defaultdict(int)

        for domino in dominoes:
            counts[tuple(sorted(domino))] += 1

        # Sum the number of pairs for each equivalent domino group
        return sum(comb(count, 2) for count in counts.values())


# @leet end
