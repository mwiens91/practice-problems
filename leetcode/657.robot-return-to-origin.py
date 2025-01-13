# @leet start
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = Counter(moves)

        return counts["L"] == counts["R"] and counts["U"] == counts["D"]


# @leet end
