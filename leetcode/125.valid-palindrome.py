# @leet start
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make lowercase and remove non-alphanumeric chars
        new_s = re.sub(r"[\W_]+", "", s.lower())

        # Check if the string is the same when it's reversed
        return new_s == new_s[::-1]


# @leet end
