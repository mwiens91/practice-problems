# @leet start
from collections import defaultdict


class Solution:
    def maxFreqSum(self, s: str) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}

        vowel_freqs: defaultdict[str, int] = defaultdict(int)
        consonant_freqs: defaultdict[str, int] = defaultdict(int)

        for char in s:
            if char in VOWELS:
                vowel_freqs[char] += 1
            else:
                consonant_freqs[char] += 1

        return max(vowel_freqs.values(), default=0) + max(
            consonant_freqs.values(), default=0
        )


# @leet end
