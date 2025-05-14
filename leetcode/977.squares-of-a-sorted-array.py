# @leet start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Take square of each value in nums
        n = len(nums)

        for i in range(n):
            nums[i] *= nums[i]

        # Find index of minimum value in nums
        min_idx = 0

        while min_idx < n - 1 and nums[min_idx] >= nums[min_idx + 1]:
            min_idx += 1

        # Now put the array in sorted order
        sorted_nums = [nums[min_idx]]

        left_idx = min_idx - 1
        right_idx = min_idx + 1

        while left_idx >= 0 and right_idx < n:
            if nums[left_idx] <= nums[right_idx]:
                sorted_nums.append(nums[left_idx])

                left_idx -= 1
            else:
                sorted_nums.append(nums[right_idx])

                right_idx += 1

        if left_idx >= 0:
            sorted_nums += nums[: left_idx + 1][::-1]
        elif right_idx < n:
            sorted_nums += nums[right_idx:]

        return sorted_nums


# @leet end
