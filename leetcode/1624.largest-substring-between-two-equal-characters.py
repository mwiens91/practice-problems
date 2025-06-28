# @leet start
from collections import Counter


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        counts = Counter(s)

        max_inner_length = -1

        for char, freq in counts.items():
            if freq < 2:
                continue

            max_inner_length = max(max_inner_length, s.rfind(char) - s.find(char) - 1)

        return max_inner_length


# @leet end
