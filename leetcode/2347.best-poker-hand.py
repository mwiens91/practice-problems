# @leet start
from collections import Counter


class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        # Flush
        if all(suit == suits[0] for suit in suits):
            return "Flush"

        # Repeated rank hands
        max_freq = max(Counter(ranks).values())

        if max_freq >= 3:
            return "Three of a Kind"

        if max_freq == 2:
            return "Pair"

        return "High Card"


# @leet end
