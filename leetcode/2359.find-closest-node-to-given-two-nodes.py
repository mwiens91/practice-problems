# @leet start
import math


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        # Note that each node has at most one edge, so each node has
        # exactly one "path". Find the distance from both node1 and
        # node2 to the nodes on their paths, stopping when we reach
        # cycles.
        NO_EDGE = -1
        NO_INTERSECTION = -1

        def get_node_distances(start: int) -> dict[int, int]:
            distances = {start: 0}

            current_node = start
            current_distance = 0

            while (
                next_node := edges[current_node]
            ) != NO_EDGE and next_node not in distances:
                current_node = next_node
                current_distance += 1

                distances[current_node] = current_distance

            return distances

        node1_distances = get_node_distances(node1)
        node2_distances = get_node_distances(node2)

        # Find the minimum of the maximum distances between both nodes
        # to a given node
        node_intersection = node1_distances.keys() & node2_distances.keys()

        min_max_distance = math.inf
        min_max_node: int | None = None

        for node in node_intersection:
            if (
                (max_distance := max(node1_distances[node], node2_distances[node]))
                < min_max_distance
                or max_distance == min_max_distance
                and node < min_max_node  # min_max_node is never None here
            ):
                min_max_distance = max_distance
                min_max_node = node

        return min_max_node if min_max_node is not None else NO_INTERSECTION


# @leet end
