# @leet start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)

        prefix_sums = [[grid[row][col] for col in range(n)] for row in range(n)]

        for row in range(n):
            for col in range(n):
                if row > 0:
                    prefix_sums[row][col] += prefix_sums[row - 1][col]

                if col > 0:
                    prefix_sums[row][col] += prefix_sums[row][col - 1]

                if row > 0 and col > 0:
                    prefix_sums[row][col] -= prefix_sums[row - 1][col - 1]

        print(prefix_sums)

        def build(row: int, col: int, n: int) -> Node:
            submat_sum = prefix_sums[row + n - 1][col + n - 1]

            if row > 0:
                submat_sum -= prefix_sums[row - 1][col + n - 1]

            if col > 0:
                submat_sum -= prefix_sums[row + n - 1][col - 1]

            if row > 0 and col > 0:
                submat_sum += prefix_sums[row - 1][col - 1]

            if submat_sum == grid[row][col] * n**2:
                return Node(
                    val=bool(grid[row][col]),
                    isLeaf=True,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None,
                )

            half_n = n // 2

            return Node(
                val=bool(grid[row][col]),
                isLeaf=False,
                topLeft=build(row, col, half_n),
                topRight=build(row, col + half_n, half_n),
                bottomLeft=build(row + half_n, col, half_n),
                bottomRight=build(row + half_n, col + half_n, half_n),
            )

        return build(0, 0, n)


# @leet end
