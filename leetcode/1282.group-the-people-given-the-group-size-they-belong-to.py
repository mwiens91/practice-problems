# @leet start
from collections import defaultdict
from itertools import chain


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups_of_size: defaultdict[int, list[list[int]]] = defaultdict(list)

        for i, group_size in enumerate(groupSizes):
            # If there are no partially filled groups of this size, make
            # a new group. Otherwise, place the index in a partially
            # filled group
            if (
                len(groups_of_size[group_size]) == 0
                or len(groups_of_size[group_size][-1]) == group_size
            ):
                groups_of_size[group_size].append([i])
            else:
                groups_of_size[group_size][-1].append(i)

        return list(chain.from_iterable(groups_of_size.values()))


# @leet end
