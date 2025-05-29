# @leet start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        CODE_POINT_A = ord("A")

        result = 0

        for i, char in enumerate(reversed(columnTitle)):
            result += (ord(char) - CODE_POINT_A + 1) * 26**i

        return result


# @leet end
