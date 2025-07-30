# @leet start
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        is_increasing = False
        is_decreasing = False
        current_run = 0
        best_run = 0

        for i in range(1, n):
            if (
                nums[i - 1] < nums[i]
                and is_increasing
                or nums[i - 1] > nums[i]
                and is_decreasing
            ):
                current_run += 1
            else:
                # Start new run
                best_run = max(best_run, current_run)

                if nums[i - 1] == nums[i]:
                    is_increasing = False
                    is_decreasing = False
                    current_run = 1
                else:
                    is_increasing = nums[i - 1] < nums[i]
                    is_decreasing = not is_increasing
                    current_run = 2

        best_run = max(best_run, current_run)

        return best_run


# @leet end
