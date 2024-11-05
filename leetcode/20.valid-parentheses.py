# @leet start
class Solution:
    def isValid(self, s: str) -> bool:
        # These will be useful later
        OPEN_BRACES = {"(", "[", "{"}
        complement_dict = {")": "(", "}": "{", "]": "["}

        # We'll use a stack to help determine validity
        stack = []

        for ch in s:
            if ch in OPEN_BRACES:
                stack.append(ch)
            else:
                # Closing brace
                if not stack or stack.pop() != complement_dict[ch]:
                    return False

        # If there's anything left in the stack, no good
        if stack:
            return False

        # Valid
        return True
# @leet end
