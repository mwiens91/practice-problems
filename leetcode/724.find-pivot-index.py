# @leet start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # Start with first index of array
        left_sum = 0
        right_sum = sum(nums) - nums[0]

        if left_sum == right_sum:
            # Found pivot index 0
            return 0

        # Try each possible other index
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                # Found pivot index
                return i

        # No pivot index
        return -1


# @leet end
