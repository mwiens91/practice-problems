# @leet start
from collections import deque
import itertools
from typing import Deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # We'll modify the matrix in place. We'll first find all 0s and
        # put them in a queue, then put all their neighbours in a queue
        # along with their distance from 0 (1), then we'll put all of
        # *their* unadded neighbours in a queue along with their
        # distance from 0 (generally 1 + the previous distance). Because
        # of the nature of breadth-first search the distance assigned is
        # always the minimum distance from 0. We repeat until all cells
        # are processed.
        num_rows = len(mat)
        num_cols = len(mat[0])

        seen_set: set[int] = set()
        queue: Deque[tuple[int, int, int]] = deque()

        # First get all zero elements
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if mat[row][col] == 0:
                queue.appendleft((row, col, 0))
                seen_set.add((row, col))

        # Do the algorithm described above
        while queue:
            # Get point from the queue and get its value
            row, col, distance = queue.pop()

            # Set the distance in the matrix
            mat[row][col] = distance

            # Enqueue adjacent points that we haven't already visited
            for adj_row, adj_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and (adj_row, adj_col) not in seen_set
                ):
                    queue.appendleft((adj_row, adj_col, distance + 1))
                    seen_set.add((adj_row, adj_col))

        # Return the matrix
        return mat


# @leet end
