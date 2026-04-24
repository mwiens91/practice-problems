# @leet start
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        SRC = 0
        DST = 1

        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for source, dest in connections:
            adj[source].append((dest, DST))
            adj[dest].append((source, SRC))

        def recurse(curr: int, prev: int) -> int:
            count = 0

            for node, direction in adj[curr]:
                if node == prev:
                    continue

                if direction == DST:
                    count += 1

                count += recurse(node, curr)

            return count

        return recurse(0, -1)


# @leet end
