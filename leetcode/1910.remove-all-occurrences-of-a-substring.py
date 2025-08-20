# @leet start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        size = len(part)
        stack: list[str] = []

        for char in s:
            stack.append(char)

            if (n := len(stack)) >= size and all(
                c == stack[i]
                for c, i in zip(reversed(part), range(n - 1, n - size - 1, -1))
            ):
                # Remove the occurance from the stack
                del stack[-size:]

        return "".join(stack)


# @leet end
