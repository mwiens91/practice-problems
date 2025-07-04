# @leet start
class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        result: list[int] = []

        total = sum(nums)
        left_sum = 0

        for num in nums:
            result.append(abs(2 * left_sum - total + num))
            left_sum += num

        return result


# @leet end
