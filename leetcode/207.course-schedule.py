# @leet start
class Solution:
    def canFinish(
        self,
        numCourses: int,  # pylint: disable=unused-argument
        prerequisites: list[list[int]],
    ) -> bool:
        # Any prerequisite scheme is valid so long as it contains no
        # cycles. For example if we need course 1 to take course 0 but
        # course 0 to take course 1, then there's no way of taking
        # either course.
        #
        # First we'll build up a hash table of edges for each node k,
        # where the node k is the key and its values are a list of other
        # nodes it is a preqrequisite for.
        edges_dict: dict[int, list[int]] = {}

        for post_node, pre_node in prerequisites:
            if pre_node in edges_dict:
                edges_dict[pre_node].append(post_node)
            else:
                edges_dict[pre_node] = [post_node]

        # Now we'll do a depth-first search on each node, starting from
        # any node that is a prerequisite to another node. We'll keep
        # track of what we've seen so far so we don't reprocess a node.
        # We'll also keep track of what nodes are on the path we've
        # traversed in a separate set.
        seen_set: set[int] = set()
        path_set: set[int] = set()

        def dfs(current_node: int) -> None:
            # Get out if we've already processed this node
            if current_node in seen_set:
                return

            # Mark this node as seen
            seen_set.add(current_node)

            # If the node has no children, get out
            if current_node not in edges_dict:
                return

            # Add node to the path and visit all children
            path_set.add(current_node)

            for child_node in edges_dict[current_node]:
                assert child_node not in path_set

                dfs(child_node)

            # Remove this node from the path
            path_set.remove(current_node)

        # Do DFS on each node
        for pre_node in edges_dict:
            try:
                dfs(pre_node)
            except AssertionError:
                return False

        return True


# @leet end
