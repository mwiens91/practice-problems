# @leet start
import itertools
import operator
import re


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        # Define a dictionary of operations
        OPERATION_DICT = {"+": operator.add, "*": operator.mul, "-": operator.sub}

        # First we'll break the expression into a list of integers and a
        # list of operators. Note that there if there are n numbers
        # there are n - 1 operators.
        nums = [int(x) for x in re.findall(r"\d+", expression)]
        operators = re.findall(r"[^\d]", expression)

        # Now define a recursive function. This takes in a left and
        # right index to the operator list performs every possible split
        # of operators. For each fork, it returns every possible
        # operation (addition/subtraction/multiplication) of numbers
        # generated in its left and right trees.

        # We'll add memoization for efficiency. We'll store tuples
        # instead of lists as values, even though the recursive function
        # returns lists.
        memo: dict[tuple[int, int], tuple[int]] = {}

        def get_all_possible_numbers(left: int, right: int) -> list[int]:
            # Try memo
            if (left, right) in memo:
                return list(memo[(left, right)])

            # Compute
            numbers = []

            # Try each operator
            for i in range(left, right + 1):
                # Get left and right tree numbers
                if left < i:
                    left_tree_numbers = get_all_possible_numbers(left, i - 1)
                else:
                    left_tree_numbers = [nums[i]]

                if i < right:
                    right_tree_numbers = get_all_possible_numbers(i + 1, right)
                else:
                    right_tree_numbers = [nums[i + 1]]

                # Perform operation on all combinations of the numbers
                for left_num, right_num in itertools.product(
                    left_tree_numbers, right_tree_numbers
                ):
                    operation = OPERATION_DICT[operators[i]]

                    numbers.append(operation(left_num, right_num))

            # Memoize and return numbers
            memo[(left, right)] = tuple(numbers)

            return numbers

        # Deal with edge case where we only have one number, no
        # operators
        if not operators:
            return nums

        # Return non-edge case result
        return get_all_possible_numbers(0, len(operators) - 1)


# @leet end
