# @leet start
class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        val = 0

        n = len(nums)

        # Process left and right numbers until we reach the middle
        left = 0
        right = n - 1

        while left < right:
            val += nums[left] * 10 ** len(str(nums[right])) + nums[right]

            left += 1
            right -= 1

        # If there is a middle number, add it to the val
        if n % 2 == 1:
            val += nums[n // 2]

        return val


# @leet end
