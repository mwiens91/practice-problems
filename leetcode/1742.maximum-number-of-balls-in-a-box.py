# @leet start
from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # NOTE: Using "digit DP" can give a better solution. I don't
        # know how to do it, too tired to learn it right now.
        box_counts: defaultdict[int, int] = defaultdict(int)

        for num in range(lowLimit, highLimit + 1):
            box_counts[sum(map(int, str(num)))] += 1

        return max(box_counts.values())


# @leet end
