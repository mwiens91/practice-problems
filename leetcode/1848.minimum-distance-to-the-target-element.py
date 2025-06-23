# @leet start
class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        # Find the maximum distance from start to the end of the array
        # (0 and n - 1)
        n = len(nums)

        max_left_delta = start
        max_right_delta = n - 1 - start

        # We are guaranteed a solution exists, so we are safe to loop
        # infinitely here and return the closest target number from
        # start which results in the minimum distance
        left_delta = 0
        right_delta = 0

        while True:
            if left_delta <= max_left_delta:
                if nums[start - left_delta] == target:
                    return left_delta

                left_delta += 1

            if right_delta <= max_right_delta:
                if nums[start + right_delta] == target:
                    return right_delta

                right_delta += 1


# @leet end
