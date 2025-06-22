# @leet start
from string import ascii_lowercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)

        return sum(1 for c in ascii_lowercase if c in chars and c.upper() in chars)


# @leet end
