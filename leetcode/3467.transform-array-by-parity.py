# @leet start
class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        num_even = 0
        num_odd = 0

        for num in nums:
            if num % 2 == 0:
                num_even += 1
            else:
                num_odd += 1

        return [0] * num_odd + [1] * num_even


# @leet end
