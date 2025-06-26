# @leet start
from itertools import chain


class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        all_nums_set = set(range(1, len(grid) ** 2 + 1))

        for num in chain.from_iterable(grid):
            if num in all_nums_set:
                all_nums_set.remove(num)
            else:
                duplicate_num = num

        missing_num = next(iter(all_nums_set))

        return [duplicate_num, missing_num]


# @leet end
