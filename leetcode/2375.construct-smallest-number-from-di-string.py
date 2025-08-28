# @leet start
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        INC = "I"

        next_digit = 1

        stack: list[str] = []
        result: list[str] = []

        # If the current direction is decreasing, we push the next digit
        # to a stack (we're *kind* of using the list like a stack
        # here). If the current direction is increasing, we reverse the
        # sequence pushed to the stack and add it to the result; then we
        # add the next digit to the result.
        for dir in pattern:
            stack.append(str(next_digit))
            next_digit += 1

            if dir == INC:
                result.extend(stack[::-1])
                stack = []

        # Handle final digit and the existing digits in the stack if we
        # were previously decreasing
        stack.append(str(next_digit))
        result.extend(stack[::-1])

        return "".join(result)


# @leet end
