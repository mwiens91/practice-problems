# @leet start
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        SEQUENCE_LENGTH = 10

        # Iterate through all SEQUENCE_LENGTH length substrings
        # (sequences) of the input string and count the occurances of
        # each sequence
        sequence_counts = defaultdict(int)

        for i in range(len(s) - SEQUENCE_LENGTH + 1):
            sequence_counts[s[i : i + SEQUENCE_LENGTH]] += 1

        return [sequence for sequence, count in sequence_counts.items() if count > 1]


# @leet end
