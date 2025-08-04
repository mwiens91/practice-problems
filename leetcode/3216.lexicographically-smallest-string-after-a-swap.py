# @leet start
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(1, len(s)):
            if s[i - 1] > s[i] and int(s[i - 1]) % 2 == int(s[i]) % 2:
                return s[: i - 1] + s[i] + s[i - 1] + s[i + 1 :]

        return s


# @leet end
