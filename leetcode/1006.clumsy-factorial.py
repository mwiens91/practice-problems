# @leet start
import operator


class Solution:
    def clumsy(self, n: int) -> int:
        # Put operations in  specific orderings
        MULTIPLY = "*"
        DIVIDE = "/"
        SUBTRACT = "-"
        ADD = "+"

        OPERATORS_EXPRESSION_ORDER = [MULTIPLY, DIVIDE, ADD, SUBTRACT]
        OPERATORS_ITERATION_ORDER = [MULTIPLY, DIVIDE, SUBTRACT, ADD]

        # Create a mapping of operator strings to operator functions
        OPERATOR_DICT = {
            MULTIPLY: operator.mul,
            DIVIDE: operator.floordiv,
            ADD: operator.add,
            SUBTRACT: operator.sub,
        }

        # Make a list of the expression elements
        stack: list[int | str] = []

        for i, num in enumerate(range(n, 0, -1)):
            stack.append(num)
            stack.append(OPERATORS_EXPRESSION_ORDER[i % 4])

        # The above loop adds one too many operators, so we pop the last
        # one
        stack.pop()

        # Perform all operations
        for target_operator in OPERATORS_ITERATION_ORDER:
            next_stack_reversed = []

            while stack:
                # Get the right operand
                right = stack.pop()

                # If there is an operation, get it, otherwise there is
                # no operation and we're done with this iteration, so we
                # put the right element onto the new stack
                if stack:
                    op = stack.pop()
                else:
                    next_stack_reversed.append(right)

                    break

                # If the operator is the target operation, perform the
                # operation and put the result back on the stack;
                # otherwise, put the right element and operator on the
                # new stack
                if op == target_operator:
                    left = stack.pop()

                    stack.append(OPERATOR_DICT[op](left, right))
                else:
                    next_stack_reversed.append(right)
                    next_stack_reversed.append(op)

            stack = next_stack_reversed[::-1]

        # Return result
        return stack[0]


# @leet end
