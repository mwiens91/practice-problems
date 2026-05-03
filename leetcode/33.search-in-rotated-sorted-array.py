# @leet start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Find smallest element, call its index "pivot"
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            # Exit early optimization
            if nums[mid] == target:
                return mid

            # Equality handles degenerate n = 1 case
            if nums[mid - 1] >= nums[mid]:
                pivot = mid
                break

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        # Find target. Do normal binary search and factor in pivot
        # when looking up mid value.
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            true_mid = (mid + pivot) % n

            if nums[true_mid] == target:
                return true_mid

            if nums[true_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# @leet end
