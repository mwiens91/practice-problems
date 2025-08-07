# @leet start
class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}

        return sum(
            1
            for i in range(left, right + 1)
            if words[i][0] in VOWELS and words[i][-1] in VOWELS
        )


# @leet end
