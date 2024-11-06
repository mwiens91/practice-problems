# @leet start
import math
from string import ascii_letters

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Here we'll keep track of the counts in t and in a sliding
        # window of s
        t_counts = {ch: 0 for ch in ascii_letters}
        s_window_counts = {ch: 0 for ch in ascii_letters}

        for ch in t:
            t_counts[ch] += 1

        # Define a function to determine if t_counts ⊆ s_window_counts
        def t_is_subset() -> bool:
            for ch, val in s_window_counts.items():
                if val < t_counts[ch]:
                    return False

            return True

        # Now we'll find the minimum sliding window such that
        # t_counts ⊆ s_window_counts
        s_length = len(s)

        start_idx = 0  # inclusive
        end_idx = 0  # exclusive
        window_length = 0

        # Keep track of the minimum window
        minimum_window_start_idx = start_idx
        minimum_window_end_idx = end_idx
        minimum_window_length = math.inf

        # Procedure is as follows: move end index forward until we find
        # a window that satisfies the subset condition; then move start
        # index forward until the subset condition is no longer
        # satisfied, then repeat
        t_length = len(t)

        while end_idx < s_length:
            # Move end_idx forward until we get a subset
            while end_idx < s_length and not t_is_subset():
                # Add the element that end_idx is pointing to
                s_window_counts[s[end_idx]] += 1

                # Update window variables
                window_length += 1
                end_idx += 1

            # Move start_idx forward until we no longer have a subset
            while t_is_subset():
                # Minimum window management
                if window_length < minimum_window_length:
                    # If we've found the theoretically smallest minimum
                    # window substring, return it now
                    if window_length == t_length:
                        return s[start_idx:end_idx]

                    # Update minimum window
                    minimum_window_length = window_length
                    minimum_window_start_idx = start_idx
                    minimum_window_end_idx = end_idx

                # Remove the element that start_idx is pointing to
                s_window_counts[s[start_idx]] -= 1

                # Update window variables
                start_idx += 1
                window_length -= 1

        # If no window substring was found, we need to return an empty
        # string
        if minimum_window_end_idx == math.inf:
            return ""

        return s[minimum_window_start_idx:minimum_window_end_idx]
# @leet end

