# @leet start
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Ensure frequencies are the same
        s_counts = Counter(s)
        goal_counts = Counter(goal)

        if s_counts != goal_counts:
            return False

        # Possible if there are exactly 0 or 2 indices that differ
        differences = sum(
            1 for s_char, goal_char in zip(s, goal) if s_char != goal_char
        )

        if differences == 0:
            # Try swapping any two of the same character if possible
            return any(freq >= 2 for freq in s_counts.values())

        if differences == 2:
            return True

        return False


# @leet end
