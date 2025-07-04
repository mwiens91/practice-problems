# @leet start
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # Go through nums, and count the number of elements smaller than
        # target and the number equal to target
        less_than_target_count = 0
        equals_target_count = 0

        for num in nums:
            if num < target:
                less_than_target_count += 1
            elif num == target:
                equals_target_count += 1

        return list(
            range(less_than_target_count, less_than_target_count + equals_target_count)
        )


# @leet end
