# @leet start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Do two binary searches. One to find the first occurance of
        # the target, and another to find the last occurance.
        n = len(nums)

        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if start == n or nums[start] != target:
            return [-1, -1]

        # Start is now equal to the index at which the first occurance
        # would occur, if it occurs
        first_position = start

        # Now find the last occurance
        start = first_position
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        second_position = end

        return [first_position, second_position]


# @leet end
