# @leet start
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0

        # Remove as many of the highest point substring first
        high_pattern, (high_points, low_points) = (
            ("ab", (x, y)) if x >= y else ("ba", (y, x))
        )

        stack: list[str] = []

        for char in s:
            if char == high_pattern[1] and stack and stack[-1] == high_pattern[0]:
                result += high_points
                stack.pop()
            else:
                stack.append(char)

        # Remove any occurances of the lower point substring
        # next—remember, this is the higher point substring but
        # reversed. We'll do the same technique as above but read from
        # the stack in reverse.
        stack_2: list[str] = []

        for char in reversed(stack):
            if char == high_pattern[1] and stack_2 and stack_2[-1] == high_pattern[0]:
                result += low_points
                stack_2.pop()
            else:
                stack_2.append(char)

        return result


# @leet end
