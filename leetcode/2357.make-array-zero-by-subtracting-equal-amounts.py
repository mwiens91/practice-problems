# @leet start
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # Suppose our array has distinct positive integers
        # x_1, x_2, ..., x_n, where x_i < x_{i + 1}. The minimum number
        # of operations is obtained by first subtracting x_1, then x_2 -
        # x_1, then x_3 - x_2, etc. There is an operation for each
        # distinct positive integer.
        return len(set(nums) - {0})


# @leet end
