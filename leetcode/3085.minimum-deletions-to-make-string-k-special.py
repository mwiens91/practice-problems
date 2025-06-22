# @leet start
from collections import Counter
import math


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = Counter(word)

        # Iterate through each letter as the smallest frequency
        # character in the final answer and find the smallest number of
        # deletions possible given this to obtain a k-special string
        min_number_deletions: float | int = math.inf

        for char in counts:
            # Get the number of deletions we need to make
            min_allowed_freq = counts[char]
            max_allowed_freq = counts[char] + k
            num_deletions_required = 0

            for freq in counts.values():
                if freq < min_allowed_freq:
                    num_deletions_required += freq
                elif freq > max_allowed_freq:
                    num_deletions_required += freq - max_allowed_freq

            min_number_deletions = min(min_number_deletions, num_deletions_required)

        return min_number_deletions


# @leet end
