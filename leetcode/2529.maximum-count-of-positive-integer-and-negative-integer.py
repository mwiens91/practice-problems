# @leet start
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)

        # Find the index of the first non-negative number
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1

        num_negative_nums = left

        # Find the index of the first positive number. We re-use the
        # left pointer from the previous binary search.
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        num_positive_nums = n - left

        return max(num_positive_nums, num_negative_nums)


# @leet end
