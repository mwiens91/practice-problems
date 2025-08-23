# @leet start
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        # Find the order that indices of the deck will be
        # revealed for this n
        n = len(deck)
        queue = deque(range(n))
        order: list[int] = []

        while queue:
            order.append(queue.popleft())

            if queue:
                queue.append(queue.popleft())

        # Arrange the deck so that cards are revealed in sorted
        # order
        result = [0] * n

        for card, idx in zip(sorted(deck), order):
            result[idx] = card

        return result


# @leet end
