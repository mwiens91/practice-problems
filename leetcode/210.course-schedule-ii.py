# @leet start
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Main idea: do a topological sort

        # First we'll build up a hash table of edges for each node k,
        # where the node k is the key and its values are a list of nodes
        # it is a preqrequisite for.
        edges_dict: dict[int, list[int]] = {}

        for child, parent in prerequisites:
            if parent in edges_dict:
                edges_dict[parent].append(child)
            else:
                edges_dict[parent] = [child]

        # Define a seen set, which we'll put all processed or
        # in-processing nodes in, and a path set, which we'll put all
        # nodes of the current path on (and remove them when they aren't
        # on the path)
        seen_set: set[int] = set()
        path_set: set[int] = set()

        # Now define a depth-first search function. After each node is
        # processed we'll add it to the back of a deque. The function
        # raises an AssertionError if it detects a cycle.
        results_deque = deque()

        def dfs(node: int) -> None:
            # Leave if we've already processed the node
            if node in seen_set:
                return

            # Mark node as seen and add node to path set
            seen_set.add(node)
            path_set.add(node)

            # Visit any children of the node
            try:
                for child in edges_dict[node]:
                    assert child not in path_set

                    dfs(child)
            except KeyError:
                # No children
                pass

            # Remove from path set and add to back of results deque
            path_set.remove(node)
            results_deque.appendleft(node)

        # Do DFS on each node
        for node in range(numCourses):
            try:
                dfs(node)
            except AssertionError:
                # Detected a cycle: unable to finish all courses
                return []

        return list(results_deque)


# @leet end
