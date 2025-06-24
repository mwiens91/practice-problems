# @leet start
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counts = Counter(text)
        balloon_counts = Counter("balloon")

        return min(text_counts[char] // balloon_counts[char] for char in balloon_counts)


# @leet end
