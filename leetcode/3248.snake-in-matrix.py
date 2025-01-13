# @leet start
from collections import Counter


class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        # Macros
        UP = "UP"
        DOWN = "DOWN"
        LEFT = "LEFT"
        RIGHT = "RIGHT"

        # Get counts of each command
        counts = Counter(commands)

        # Determine final position
        final_row = counts[DOWN] - counts[UP]
        final_col = counts[RIGHT] - counts[LEFT]

        return final_row * n + final_col


# @leet end
