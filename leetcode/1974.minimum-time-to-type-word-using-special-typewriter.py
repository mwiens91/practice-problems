# @leet start
class Solution:
    def minTimeToType(self, word: str) -> int:
        turns = 0

        for prev_char, char in zip('a' + word, word):
            turns += min(
                (ord(char) - ord(prev_char)) % 26,
                (ord(prev_char) - ord(char)) % 26,
            )

        return turns + len(word)


# @leet end
