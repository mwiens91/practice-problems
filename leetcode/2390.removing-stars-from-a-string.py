# @leet start
class Solution:
    def removeStars(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# @leet end
