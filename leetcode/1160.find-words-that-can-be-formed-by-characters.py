# @leet start
from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_counter = Counter(chars)

        sum_of_good_string_lengths = 0

        for word in words:
            if Counter(word) <= chars_counter:
                sum_of_good_string_lengths += len(word)

        return sum_of_good_string_lengths


# @leet end
