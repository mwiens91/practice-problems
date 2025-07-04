# @leet start
from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        # Get digit characters that have counts equal to the digit
        # itself
        counts = Counter(s)
        digits_with_valid_freqs = {d for d in counts if counts[d] == int(d)}

        for ch_1, ch_2 in zip(s, s[1:]):
            if (
                ch_1 != ch_2
                and ch_1 in digits_with_valid_freqs
                and ch_2 in digits_with_valid_freqs
            ):
                return ch_1 + ch_2

        return ""


# @leet end
