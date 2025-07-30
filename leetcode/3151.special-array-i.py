# @leet start
class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        first_num_mod_2 = nums[0] % 2

        return all(num % 2 == ((i + first_num_mod_2) % 2) for i, num in enumerate(nums))


# @leet end
