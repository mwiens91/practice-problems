# @leet start
class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even_num_gen = (num for num in nums if num % 2 == 0)
        odd_num_gen = (num for num in nums if num % 2 == 1)

        return [num for pair in zip(even_num_gen, odd_num_gen) for num in pair]


# @leet end
