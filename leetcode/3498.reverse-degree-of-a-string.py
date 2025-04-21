# @leet start
class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((1 + ord("z") - ord(char)) * (i + 1) for i, char in enumerate(s))


# @leet end
