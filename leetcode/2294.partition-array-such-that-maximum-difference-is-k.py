# @leet start
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        # First sort the numbers
        nums.sort()

        # Then find the number of intervals required
        num_intervals = 1
        current_interval_end = nums[0] + k

        for num in nums:
            if num > current_interval_end:
                num_intervals += 1
                current_interval_end = num + k

        return num_intervals


# @leet end
