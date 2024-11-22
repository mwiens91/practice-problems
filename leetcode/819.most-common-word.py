# @leet start
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned_set = set(banned)

        valid_words = [
            word.lower()
            for word in re.findall(r"\b\w+\b", paragraph)
            if word.lower() not in banned_set
        ]

        return max(set(valid_words), key=valid_words.count)


# @leet end
