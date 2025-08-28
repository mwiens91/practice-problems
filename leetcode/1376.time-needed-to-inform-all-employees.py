# @leet start
from collections import defaultdict


class Solution:
    def numOfMinutes(
        self,
        n: int,  # pylint: disable=unused-argument
        headID: int,
        manager: list[int],
        informTime: list[int],
    ) -> int:
        edges: defaultdict[int, list[int]] = defaultdict(list)

        for child, parent in enumerate(manager):
            edges[parent].append(child)

        def get_transmission_time(node: int) -> int:
            if node not in edges:
                return 0

            return informTime[node] + max(map(get_transmission_time, edges[node]))

        return get_transmission_time(headID)


# @leet end
