# @leet start
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # Find the first i such that arr[i] > arr[i + 1]. Note that for
        # a mountain array i cannot be the first or last index.
        left = 1
        right = len(arr) - 2

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

        return left


# @leet end
