# @leet start
class Solution:
    def finalString(self, s: str) -> str:
        result: list[str] = []

        for char in s:
            if char == "i":
                result = result[::-1]
            else:
                result.append(char)

        return "".join(result)


# @leet end
