# @leet start
from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Go through s, keeping track of what is in the current
        # substring with a hash table containing what we've seen so far
        # and where we've seen it
        best = 0
        chars_seen = set()
        substr_deque = deque()

        for char in s:
            print(substr_deque)
            if char in chars_seen:
                # Compare best with the substring that we can no longer
                # continue
                best = max(best, len(substr_deque))

                # Reset. Pop everything before the repeated character
                # out of the substring dequeue, and remove it from the
                # characters seen set. Finally, pop out the repeated
                # character from the left.
                while (oldest_char := substr_deque.popleft()) != char:
                    chars_seen.remove(oldest_char)

                substr_deque.append(char)

            else:
                # Still a valid substring
                chars_seen.add(char)
                substr_deque.append(char)

        # Compare best with the final substring length
        best = max(best, len(substr_deque))

        return best


# @leet end
