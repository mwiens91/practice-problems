# @leet start
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        adj_lists: dict[int, list[int]] = {}
        in_degree: dict[int, int] = {}

        for a, b in edges:
            if a not in adj_lists:
                adj_lists[a] = []

            if b not in adj_lists:
                adj_lists[b] = []

            adj_lists[a].append(b)
            adj_lists[b].append(a)

            in_degree[a] = in_degree.get(a, 0) + 1
            in_degree[b] = in_degree.get(b, 0) + 1

        layer = [k for k, v in in_degree.items() if v == 1]
        visited = set(layer)

        while layer:
            next_layer: list[int] = []

            for node in layer:
                for adj_node in adj_lists[node]:
                    if adj_node in visited:
                        continue

                    in_degree[adj_node] -= 1

                    if in_degree[adj_node] == 1:
                        next_layer.append(adj_node)
                        visited.add(adj_node)

            layer = next_layer

        remaining_nodes = set(in_degree.keys()) - visited

        # We need to return whatever redundant edge appears last in the
        # input
        for edge in reversed(edges):
            if edge[0] in remaining_nodes and edge[1] in remaining_nodes:
                return edge


# @leet end
