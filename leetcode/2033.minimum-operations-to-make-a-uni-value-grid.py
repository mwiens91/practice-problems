# @leet start
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Get all elements from the grid
        nums: list[int] = []

        for row in grid:
            nums += row

        # Check if a solution is possible. Return failure code -1 if it
        # is not possible.
        required_mod_x_value = nums[0] % x

        for num in nums:
            if num % x != required_mod_x_value:
                return -1

        # Find the median. If n is odd, use the true median. If n is
        # even, use the element to the right of the median (we could
        # also use the left—doesn't matter).
        nums.sort()

        median = nums[len(nums) // 2]

        # The minimum number of operations is the number of operations
        # to bring all elements to the median value. Count this and
        # return it.
        return sum(abs(num - median) // x for num in nums)


# @leet end
