# @leet start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return list(bin(start ^ goal)).count("1")


# @leet end
