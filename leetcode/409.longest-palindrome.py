# @leet start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Get counts of characters in s
        counts = Counter(s)

        # Keep track of whether we've found an odd count
        found_odd_count = False

        # Find length of longest palindrome
        longest_palindrome = 0

        for val in counts.values():
            if not found_odd_count and val % 2 == 1:
                found_odd_count = True

            # Add each pair of characters
            longest_palindrome += (val // 2) * 2

        # If we found an odd count, we can put another character in the
        # middle of the palndrome
        if found_odd_count:
            longest_palindrome += 1

        return longest_palindrome


# @leet end
