# @leet start
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Find the median value. If n is odd we use the true median.
        # Otherwise we can use the element to the right of the median
        # (the left would work too).
        nums.sort()

        median = nums[len(nums) // 2]

        # The minimum number of moves is the number of moves required to
        # bring all elements to the median value
        return sum(abs(num - median) for num in nums)


# @leet end
