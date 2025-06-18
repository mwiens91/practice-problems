# @leet start
class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(char: str, x: int) -> str:
            return chr(ord(char) + x)

        result = list(s)

        # Replace digits with shifted chars
        for i in range(1, len(s), 2):
            result[i] = shift(result[i - 1], int(result[i]))

        return "".join(result)


# @leet end
