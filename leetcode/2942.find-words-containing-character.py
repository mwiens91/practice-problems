# @leet start
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        result: list[int] = []

        for i, word in enumerate(words):
            if x in word:
                result.append(i)

        return result


# @leet end
