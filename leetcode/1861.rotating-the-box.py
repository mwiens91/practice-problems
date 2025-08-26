# @leet start
from collections import deque


class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        STONE = "#"
        OBSTACLE = "*"
        EMPTY = "."

        row_length = len(boxGrid[0])

        # Move the stones before rotating
        for row in boxGrid:
            available_idxs_queue: deque[int] = deque([])

            for i in range(row_length - 1, -1, -1):
                if row[i] == STONE:
                    if available_idxs_queue:
                        # Move stone and mark its former position as
                        # available
                        row[i] = EMPTY
                        row[available_idxs_queue.popleft()] = STONE

                        available_idxs_queue.append(i)
                elif row[i] == OBSTACLE:
                    # Can't move stones below the obstacle
                    available_idxs_queue = deque([])
                else:
                    # Empty space
                    available_idxs_queue.append(i)

        return [list(row) for row in zip(*boxGrid[::-1])]


# @leet end
