# @leet start
class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        position = 0
        on_boundary_count = 0  # we don't count starting on boundary

        for num in nums:
            position += num

            if position == 0:
                on_boundary_count += 1

        return on_boundary_count


# @leet end
