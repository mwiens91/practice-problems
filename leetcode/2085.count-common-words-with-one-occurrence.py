# @leet start
from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        # Make counters of both arrays: to make this function faster we
        # assign counter1 to the array with less words, and counter2 to
        # the array with more words
        if len(words1) < len(words2):
            counter1 = Counter(words1)
            counter2 = Counter(words2)
        else:
            counter1 = Counter(words2)
            counter2 = Counter(words1)

        # Now count words they have in common that are distinct
        num_shared_distinct = 0

        for word in counter1:
            if word in counter2 and counter1[word] == counter2[word] == 1:
                num_shared_distinct += 1

        return num_shared_distinct


# @leet end
