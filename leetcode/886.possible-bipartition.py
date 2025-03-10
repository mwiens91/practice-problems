# @leet start
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def possibleBipartition(
        self, n: int, dislikes: list[list[int]]  # pylint: disable=unused-argument
    ) -> bool:
        # Build adjacency lists for an undirected graph where an edge
        # between two people (hereafter referred to as nodes) indicates that
        # the people cannot be placed in the same group. We need to make
        # sure that the graph does not have odd cycles, which is
        # equivalent to ensuring that we can colour each node red or
        # black without having adjacent nodes being the same colour.
        adjacency_list_dict: DefaultDict[int, list[int]] = defaultdict(list)

        for person_a, person_b in dislikes:
            adjacency_list_dict[person_a].append(person_b)
            adjacency_list_dict[person_b].append(person_a)

        # For each node we colour it red or black. We colour its
        # neighbours the opposite colour. If a neighbour has a colour
        # already, we assert that it is the opposite colour.
        BLACK = "black"
        RED = "red"

        colour_dict: dict[int, None | str] = {
            node: None for node in adjacency_list_dict
        }

        # Put nodes we've already processed in here
        processed_set: set[int] = set()

        # Each initial use of DFS on a node will colour all nodes in the
        # same component. Prior to running the DFS on a node, set the
        # node colour to either black or red.
        def dfs(node: int) -> None:
            # Mark this node as processed
            processed_set.add(node)

            # For each neighbour, if it hasn't been processed, colour it
            # with the opposite colour and run DFS on it; if it has been
            # processed, assert that its colour is the opposite colour
            opposite_colour = RED if colour_dict[node] == BLACK else BLACK

            for neighbour in adjacency_list_dict[node]:
                if neighbour in processed_set:
                    assert colour_dict[neighbour] == opposite_colour
                else:
                    colour_dict[neighbour] = opposite_colour

                    dfs(neighbour)

        # Run DFS on each node that isn't processed already
        for node in adjacency_list_dict:
            if node not in processed_set:
                # Set the node colour
                colour_dict[node] = BLACK

                # DFS
                try:
                    dfs(node)
                except AssertionError:
                    # Odd cycle detected
                    return False

        # No odd cycles detected
        return True


# @leet end
