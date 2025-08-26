# @leet start
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0

        for i, freq in enumerate(sorted(Counter(word).values(), reverse=True)):
            count += freq * (i // 8 + 1)

        return count


# @leet end
