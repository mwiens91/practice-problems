# @leet start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        # Find nodes with zero-in-degree
        return list(set(range(n)).difference(edge[1] for edge in edges))


# @leet end
