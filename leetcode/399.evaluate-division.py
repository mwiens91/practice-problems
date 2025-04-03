# @leet start
from collections import deque


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        # Using the hint, we treat this as a graph problem. Since for
        # each i, equations[i][0] / equations[i][1] = values[i], we can
        # assign a directed edge with weight values[i] between the
        # numerator and denominator, and a directed edge with weight
        # 1 / values[i] between denominator and numerator.
        adjacency_lists: dict[str, list[tuple[str, float]]] = {}

        for i, (numerator, denominator) in enumerate(equations):
            forward_edge = (denominator, values[i])
            backward_edge = (numerator, 1 / values[i])

            if numerator in adjacency_lists:
                adjacency_lists[numerator].append(forward_edge)
            else:
                adjacency_lists[numerator] = [forward_edge]

            if denominator in adjacency_lists:
                adjacency_lists[denominator].append(backward_edge)
            else:
                adjacency_lists[denominator] = [backward_edge]

        # Define a function which finds the value of the equation x / y,
        # which is equivalent to the product of edge weights between any
        # path from x to y. If no such path exists, we return -1.
        def find_value(start: str, end: str) -> float:
            # Edge cases:
            # - if the start node or end node is not in the adjacency
            #   lists, return -1 (note: we don't need the second check,
            #   but it potentially saves work)
            # - if the start node is the end node, return 1
            if start not in adjacency_lists or end not in adjacency_lists:
                return -1

            if start == end:
                return 1

            # Initialize a queue with the starting edges and also an
            # visited set to track which nodes we've visited/enqueued.
            queue: deque[tuple[str, float]] = deque(adjacency_lists[start])
            visited: set[str] = {start, *(node for node, _ in adjacency_lists[start])}

            while queue:
                node, path_weight = queue.popleft()

                # Found endpoint
                if node == end:
                    return path_weight

                for neighbour, edge_weight in adjacency_lists[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, path_weight * edge_weight))
                        visited.add(neighbour)

            # Could not find endpoint
            return -1

        # Find the value of each query
        return [find_value(start, end) for start, end in queries]


# @leet end
