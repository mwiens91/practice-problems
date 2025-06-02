# @leet start
from collections import defaultdict


class Solution:
    def mergeSimilarItems(
        self, items1: list[list[int]], items2: list[list[int]]
    ) -> list[list[int]]:
        value_weights: defaultdict[int, int] = defaultdict(int)

        for items in [items1, items2]:
            for value, weight in items:
                value_weights[value] += weight

        return sorted(map(list, value_weights.items()))


# @leet end
