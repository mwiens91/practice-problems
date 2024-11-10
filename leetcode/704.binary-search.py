# @leet start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Do a binary search
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            mid_num = nums[mid]

            if mid_num == target:
                return mid

            if mid_num > target:
                right = mid - 1
            else:
                left = mid + 1

        # No target
        return -1


# @leet end
