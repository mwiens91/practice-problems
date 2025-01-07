# @leet start
from collections import Counter
from operator import itemgetter


class Solution:
    def frequencySort(self, s: str) -> str:
        # Get counts of characters
        counts = Counter(s)

        # Sort counts in decreasing frequency order and build the
        # sorted string
        counts_tuples = list(counts.items())
        counts_tuples.sort(key=itemgetter(1), reverse=True)

        result_chars = []

        for char, count in counts_tuples:
            result_chars += [char] * count

        return "".join(result_chars)


# @leet end
