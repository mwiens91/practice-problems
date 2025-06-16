# @leet start
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        # NOTE: you can do this solution with a single iteration in O(1)
        # space. The idea is for each number, if it is greater than the
        # minimum seen so far, update the maximum difference, otherwise,
        # if it is less than the minimum seen so far, update the
        # minimum. I am doing three iterations in O(n) space with a
        # different method. I just want to move on and I kind of like
        # this solution anyway, even if it's less efficient.

        # Get prefix mins and suffix maxes
        n = len(nums)

        prefix_mins = [nums[0]] * n

        for i in range(1, n):
            prefix_mins[i] = min(prefix_mins[i - 1], nums[i])

        suffix_maxes = [nums[-1]] * n

        for i in range(n - 2, -1, -1):
            suffix_maxes[i] = max(suffix_maxes[i + 1], nums[i])

        # Get the maximum difference, such that the max number is
        # greater than the min number. If no such pairing exists, we
        # return -1.
        max_difference = -1

        for i in range(n - 1):
            if (this_difference := suffix_maxes[i + 1] - prefix_mins[i]) > 0:
                max_difference = max(max_difference, this_difference)

        return max_difference


# @leet end
