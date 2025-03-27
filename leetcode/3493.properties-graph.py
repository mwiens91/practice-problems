# @leet start
from collections import deque
import itertools


class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        # First for each node (property) build a set containing its
        # unique elements
        n = len(properties)

        node_element_sets = {i: set(properties[i]) for i in range(n)}

        # Now find edges between nodes and build adjacency lists
        adjacency_list_dict = {i: [] for i in range(n)}

        for node_1, node_2 in itertools.combinations(range(n), 2):
            # Two nodes have an undirected edge if they have k or more
            # elements in common
            if len(node_element_sets[node_1] & node_element_sets[node_2]) >= k:
                adjacency_list_dict[node_1].append(node_2)
                adjacency_list_dict[node_2].append(node_1)

        # Now find the number of connected components using BFS
        visited: set[int] = set()

        def visit_connected_component(start_node: int) -> None:
            queue = deque([start_node])

            while queue:
                node = queue.popleft()

                visited.add(node)

                for neighbour in adjacency_list_dict[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)

        num_connected_components = 0

        for node in range(n):
            if node not in visited:
                visit_connected_component(node)
                num_connected_components += 1

        return num_connected_components


# @leet end
