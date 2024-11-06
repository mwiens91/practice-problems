# @leet start
import itertools
from string import ascii_lowercase

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get lengths. If s1 is longer than s2 we can return False.
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        # Make counters of characters in s1, and also of characters in a
        # sliding window of length n1 of s2.
        s1_count = {ch: 0 for ch in ascii_lowercase}
        s2_sliding_count = {ch: 0 for ch in ascii_lowercase}

        for ch in s1:
            s1_count[ch] += 1

        for ch in itertools.islice(s2, n1):
            s2_sliding_count[ch] += 1

        # Test for equality now. We'll also do this in the loop below.
        if s1_count == s2_sliding_count:
            return True

        # Slide the window
        for new_end_idx in range(n1, n2):
            old_start_idx = new_end_idx - n1

            new_ch = s2[new_end_idx]
            old_ch = s2[old_start_idx]

            s2_sliding_count[new_ch] += 1
            s2_sliding_count[old_ch] -= 1

            if s1_count == s2_sliding_count:
                return True

        # Didn't find a permutation
        return False
# @leet end
