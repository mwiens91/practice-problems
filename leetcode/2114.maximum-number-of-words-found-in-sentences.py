# @leet start
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(map(len, map(str.split, sentences)))


# @leet end
