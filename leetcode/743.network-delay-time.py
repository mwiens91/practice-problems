# @leet start
import heapq
import math


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_lists: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for src, dest, weight in times:
            adj_lists[src - 1].append((dest - 1, weight))

        dists = [math.inf] * n
        dists[k - 1] = 0
        heap = [(0, k - 1)]

        while heap:
            dist, node = heapq.heappop(heap)

            if dists[node] < dist:
                continue

            for dest, weight in adj_lists[node]:
                new_dest_dist = dist + weight

                if new_dest_dist < dists[dest]:
                    dists[dest] = new_dest_dist
                    heapq.heappush(heap, (new_dest_dist, dest))

        max_dist = max(dists)

        return max_dist if max_dist < math.inf else -1


# @leet end
