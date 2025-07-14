# @leet start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(map(len, (a, b)))


# @leet end
