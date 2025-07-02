# @leet start
from string import ascii_uppercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        s_char_set = set(s)

        for upper_letter in reversed(ascii_uppercase):
            if upper_letter in s_char_set and upper_letter.lower() in s_char_set:
                return upper_letter

        return ""


# @leet end
