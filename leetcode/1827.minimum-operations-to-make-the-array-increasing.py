# @leet start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        result = 0

        prev_value = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > prev_value:
                prev_value = nums[i]
            else:
                result += prev_value + 1 - nums[i]
                prev_value += 1

        return result


# @leet end
