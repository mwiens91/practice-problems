# @leet start
from string import ascii_lowercase


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # Using a sliding window here and a hash table for character
        # counts in the sliding window of s and p
        s_counts = {ch: 0 for ch in ascii_lowercase}
        p_counts = {ch: 0 for ch in ascii_lowercase}

        # Populate p_counts, this won't change
        for char in p:
            p_counts[char] += 1

        # Find the initial sliding window counts for s, we'll change
        # this later in a loop
        p_len = len(p)

        for char in s[:p_len]:
            s_counts[char] += 1

        # Store the results
        results = []

        if p_counts == s_counts:
            results.append(0)

        # Slide the window
        s_len = len(s)

        for i in range(1, s_len - p_len + 1):
            # Remove old
            s_counts[s[i - 1]] -= 1

            # Add new
            s_counts[s[i + p_len - 1]] += 1

            # Check if there's a match
            if p_counts == s_counts:
                results.append(i)

        return results


# @leet end
