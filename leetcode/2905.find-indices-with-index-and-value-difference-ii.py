# @leet start
class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        # NOTE: Same as my solution for LC 2903. That one has some
        # comments.
        n = len(nums)

        prefix_min = (nums[0], 0)
        prefix_max = (nums[0], 0)

        for i in range(indexDifference, n):
            if abs(prefix_min[0] - nums[i]) >= valueDifference:
                return [prefix_min[1], i]

            if abs(prefix_max[0] - nums[i]) >= valueDifference:
                return [prefix_max[1], i]

            if (next_prefix_idx := i - indexDifference + 1) < n:
                if nums[next_prefix_idx] > prefix_max[0]:
                    prefix_max = (nums[next_prefix_idx], next_prefix_idx)
                elif nums[next_prefix_idx] < prefix_min[0]:
                    prefix_min = (nums[next_prefix_idx], next_prefix_idx)

        return [-1, -1]


# @leet end
