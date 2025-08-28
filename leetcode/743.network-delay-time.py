# @leet start
from collections import defaultdict
import heapq
import math


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        for from_node, to_node, weight in times:
            edges[from_node].append((weight, to_node))

        time_from_src = {i: math.inf for i in range(1, n + 1)}
        time_from_src[k] = 0

        heap = [(0, k)]

        while heap:
            t, node = heapq.heappop(heap)

            if time_from_src[node] < t:
                continue

            for weight, to_node in edges[node]:
                new_t = t + weight

                if new_t < time_from_src[to_node]:
                    time_from_src[to_node] = new_t
                    heapq.heappush(heap, (new_t, to_node))

        delay_time = max(time_from_src.values())

        return delay_time if delay_time < math.inf else -1


# @leet end
