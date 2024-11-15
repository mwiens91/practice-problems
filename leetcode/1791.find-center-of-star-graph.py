# @leet start
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # Intuition: in the star graph, the vertex is the only node to
        # appear move than once. So if we see a node with more than one
        # edge, it's the center
        seen_set = set()

        for u, v in edges:
            if u in seen_set:
                return u

            if v in seen_set:
                return v

            seen_set.update((u, v))
# @leet end
