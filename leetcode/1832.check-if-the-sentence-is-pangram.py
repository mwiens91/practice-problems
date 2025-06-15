# @leet start
from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(ascii_lowercase) == set(sentence)


# @leet end
