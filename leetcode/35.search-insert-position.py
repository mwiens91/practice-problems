# @leet start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Do a binary search
        n = len(nums)

        # With the below approach, if at the end of the loop
        # start == n - 1, either (1) start is the correct index to
        # return or (2) the target is greater than the last element with
        # index n - 1, so we need to return n instead. We'll just check
        # for that here.
        if target > nums[n - 1]:
            return n

        # Perform binary search which works correctly for
        # target < nums[n - 1]
        start = 0
        end = n - 1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return start


# @leet end
