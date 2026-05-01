# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        BRACE_DICT = {")": "(", "}": "{", "]": "["}
        stack: list[str] = []

        for ch in s:
            if ch in BRACE_DICT:
                if not stack or stack[-1] != BRACE_DICT[ch]:
                    return False

                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


# @leet end
