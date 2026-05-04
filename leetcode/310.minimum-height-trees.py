# @leet start
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        indegree = [0] * n
        adj_lists: list[list[int]] = [[] for _ in range(n)]

        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1

            adj_lists[a].append(b)
            adj_lists[b].append(a)

        layer = [nd for nd in range(n) if indegree[nd] == 1]

        while True:
            next_layer: list[int] = []

            for nd in layer:
                for adj_nd in adj_lists[nd]:
                    indegree[adj_nd] -= 1

                    if indegree[adj_nd] == 1:
                        next_layer.append(adj_nd)

            if not next_layer:
                return layer

            layer = next_layer


# @leet end
