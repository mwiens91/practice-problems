# @leet start
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return [
            num
            for num_list in [[int(x) for x in str(num)] for num in nums]
            for num in num_list
        ]


# @leet end
