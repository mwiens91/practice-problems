# @leet start
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Build an adjacency list dictionary
        adjacency_list_dict: DefaultDict[int, list[int]] = defaultdict(list)

        for n1, n2 in edges:
            adjacency_list_dict[n1].append(n2)
            adjacency_list_dict[n2].append(n1)

        # Define a depth first search function which takes any node of a
        # connected component and returns whether the connected
        # component is complete. Note: we only call the function on
        # nodes in connected components that have not been visited.
        visited: set[int] = set()

        def is_connected_component_complete(node: int) -> bool:
            # Find the number of nodes and edges in the component
            component_num_nodes = 0
            component_num_edges = 0

            def dfs(node: int) -> None:
                nonlocal component_num_nodes, component_num_edges

                # Mark this node as visited
                visited.add(node)

                # Add to the component's number of nodes and edges.
                # Because each undirected edge will be counted twice, we
                # treat each count of a directed edge as half an edge
                # count.
                component_num_nodes += 1
                component_num_edges += len(adjacency_list_dict[node]) / 2

                # Visit unvisited neighbours
                for neighbour in adjacency_list_dict[node]:
                    if neighbour not in visited:
                        dfs(neighbour)

            dfs(node)

            # Determine if this is a complete connected component, which
            # is determined by the component having edges equal to the
            # maximum number of unique pairs of nodes
            return (
                component_num_edges
                == component_num_nodes * (component_num_nodes - 1) / 2
            )

        # Count the number of complete connected components
        num_complete_connected_components = 0

        for node in range(n):
            if node not in visited:
                num_complete_connected_components += int(
                    is_connected_component_complete(node)
                )

        return num_complete_connected_components


# @leet end
