# @leet start
class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        return [word for line in words for word in line.split(separator) if word != ""]


# @leet end
