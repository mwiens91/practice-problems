# @leet start
import heapq
import math


class Solution:
    def findTheCity(
        self, n: int, edges: list[list[int]], distanceThreshold: int
    ) -> int:
        adj_lists: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for src, dst, weight in edges:
            adj_lists[src].append((dst, weight))
            adj_lists[dst].append((src, weight))

        def helper(start: int):
            dists = [math.inf for _ in range(n)]
            dists[start] = 0
            heap = [(0, start)]
            count = 0

            while heap:
                dist, node = heapq.heappop(heap)

                if dist > dists[node]:
                    continue

                count += 1

                for adj, weight in adj_lists[node]:
                    adj_dist = dist + weight

                    if adj_dist <= distanceThreshold and adj_dist < dists[adj]:
                        dists[adj] = adj_dist
                        heapq.heappush(heap, (adj_dist, adj))

            return count

        best_city = -1
        min_connections = n

        for i in range(n):
            connections = helper(i)

            if connections <= min_connections:
                best_city = i
                min_connections = connections

        return best_city


# @leet end
