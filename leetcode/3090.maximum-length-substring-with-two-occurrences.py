# @leet start
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Use a sliding window
        counts: defaultdict[str, int] = defaultdict(int)

        max_length = 0
        left = 0

        # For each right endpoint, contract the left endpoint until the
        # conditions are met
        for endpoint, char in enumerate(s):
            counts[char] += 1

            while counts[char] > 2:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, endpoint - left + 1)

        return max_length


# @leet end
