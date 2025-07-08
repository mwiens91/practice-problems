# @leet start
class Solution:
    def averageValue(self, nums: list[int]) -> int:
        divisible_by_six = [num for num in nums if num % 6 == 0]

        return sum(divisible_by_six) // len(divisible_by_six) if divisible_by_six else 0


# @leet end
