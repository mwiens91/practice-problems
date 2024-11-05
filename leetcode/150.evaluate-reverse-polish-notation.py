# @leet start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # NOTE: I didn't actually read what Reverse Polish notation is,
        # I'm just trying to infer it from the examples—crossing my
        # fingers and hoping it works

        # Make functions for the operations
        operations_dict = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        # Use a stack here
        stack = []

        for token in tokens:
            if token in operations_dict:
                y = stack.pop()
                x = stack.pop()

                res = operations_dict[token](x, y)

                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
# @leet end

