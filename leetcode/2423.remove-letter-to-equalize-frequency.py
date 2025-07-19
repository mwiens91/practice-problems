# @leet start
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        # For this to be possible we either need
        # - 1. exactly one character
        # - 2. all but possibly one character have a given frequency f
        # one character has a frequency 1
        # - 3. all but one character to have a frequency f and one
        # character to have a frequency f + 1
        freqs = Counter(word).values()

        # Test if there is exactly 1 character
        if len(freqs) == 1:
            return True

        # Test if all characters have frequency 1
        freqs_set = set(freqs)

        if len(freqs_set) == 1 and next(iter(freqs_set)) == 1:
            return True

        # Test if there are 2 frequencies, either
        # - 1 frequency of 1, n - 1 frequencies of f
        # - 1 frequency of f + 1, n - 1 frequencies of f
        count_of_freqs = Counter(freqs)

        if len(count_of_freqs) == 2:
            (f1, f1_freq), (f2, f2_freq) = sorted(count_of_freqs.items())

            if f1 == f1_freq == 1 or f2 - f1 == f2_freq == 1:
                return True

        return False


# @leet end
