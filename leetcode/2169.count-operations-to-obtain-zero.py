# @leet start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        num_operations = 0

        while num1 * num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1

            num_operations += 1

        return num_operations


# @leet end
