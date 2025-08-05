# @leet start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# @leet end
