# @leet start
from collections import deque
from string import ascii_uppercase

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # NOTE: For this solution you really don't need a deque, just
        # keep track of the start index and end index using a "sliding
        # window" type technique. Also probably just move the
        # substr_is_valid logic outside of a function call? Lots of
        # little efficiencies here, but I got the time and memory
        # complexity I want, so I'm just going to move on instead of
        # making this super clean.

        # Keep track of the count of letters in the substring
        count_dict = {ch: 0 for ch in ascii_uppercase}

        # Define a function that tells us if the current substring is
        # valid using the count_dict. There's probably a better way to
        # do this but it's still O(1) so we're good.
        def substr_is_valid():
            max_count = max(count_dict.values())

            if len(substr_deque) > max_count + k:
                return False

            return True

        # Keep the substring in a deque
        substr_deque = deque()

        # Go through all valid substrings, find the best one
        best = 0

        for char in s:
            # Process new character
            substr_deque.append(char)
            count_dict[char] += 1

            # Pop out old characters until the substring is valid
            while not substr_is_valid():
                old_char = substr_deque.popleft()
                count_dict[old_char] -= 1

            # Update the result variable
            best = max(best, len(substr_deque))

        return best
# @leet end

