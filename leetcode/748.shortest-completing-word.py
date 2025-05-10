# @leet start
from collections import Counter
import math
import re


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Get counts of lowercase alphabetic characters
        license_letter_counts = Counter(re.sub(r"[^a-zA-Z]", "", licensePlate).lower())

        # Find the shortest completing word
        best_word: str | None = None
        best_word_length = math.inf

        # Assume all words are lowercase
        for word in words:
            if (
                license_letter_counts <= Counter(word)
                and (word_len := len(word)) < best_word_length
            ):
                best_word = word
                best_word_length = word_len

        return best_word


# @leet end
