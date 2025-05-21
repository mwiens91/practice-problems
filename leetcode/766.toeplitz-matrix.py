# @leet start
from collections import deque


class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # Hold the previous row elements in a queue. Iterate over all
        # other rows in order. For each row, we modify the queue so that
        # it contains the elements that the matrix would have in that
        # row if it was Toeplitz.
        queue = deque(matrix[0])

        for i in range(1, len(matrix)):
            queue.appendleft(matrix[i][0])
            queue.pop()

            if list(queue) != matrix[i]:
                return False

        return True


# @leet end
