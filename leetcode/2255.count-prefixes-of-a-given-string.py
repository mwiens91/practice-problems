# @leet start
class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        return sum(int(s.startswith(word)) for word in words)


# @leet end
