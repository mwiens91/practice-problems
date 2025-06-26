# @leet start
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        increment_ops = {"X++", "++X"}

        value = 0

        for op in operations:
            if op in increment_ops:
                value += 1
            else:
                value -= 1

        return value


# @leet end
