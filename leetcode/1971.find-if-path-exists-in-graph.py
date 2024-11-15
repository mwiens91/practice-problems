# @leet start
from collections import deque


class Solution:
    def validPath(
        self,
        n: int,  # pylint: disable=unused-argument
        edges: list[list[int]],
        source: int,
        destination: int,
    ) -> bool:
        # Build adjacency lists
        adjacency_dict = {}

        for u, v in edges:
            if u in adjacency_dict:
                adjacency_dict[u].append(v)
            else:
                adjacency_dict[u] = [v]

            if v in adjacency_dict:
                adjacency_dict[v].append(u)
            else:
                adjacency_dict[v] = [u]

        # Handle edge cases
        if source == destination:
            return True

        if source not in adjacency_dict:
            return False

        # Do a BFS
        visited = {source}
        queue = deque([source])

        while queue:
            vertex = queue.pop()

            if vertex == destination:
                return True

            for adjacent_vertex in adjacency_dict[vertex]:
                if adjacent_vertex not in visited:
                    queue.appendleft(adjacent_vertex)
                    visited.add(adjacent_vertex)

        return False


# @leet end
