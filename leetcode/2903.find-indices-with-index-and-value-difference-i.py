# @leet start
class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        # Compare each number with the largest and smallest numbers it
        # is at least indexDifference indices away from
        n = len(nums)

        prefix_min = (nums[0], 0)
        prefix_max = (nums[0], 0)

        for i in range(indexDifference, n):
            if abs(prefix_min[0] - nums[i]) >= valueDifference:
                return [prefix_min[1], i]

            if abs(prefix_max[0] - nums[i]) >= valueDifference:
                return [prefix_max[1], i]

            # Update prefix min and max
            if (next_prefix_idx := i - indexDifference + 1) < n:
                if nums[next_prefix_idx] > prefix_max[0]:
                    prefix_max = (nums[next_prefix_idx], next_prefix_idx)
                elif nums[next_prefix_idx] < prefix_min[0]:
                    prefix_min = (nums[next_prefix_idx], next_prefix_idx)

        return [-1, -1]


# @leet end
