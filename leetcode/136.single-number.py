# @leet start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # NOTE: needed Neetcode to understand to use and understand XOR
        # solution

        # XOR everything together
        res = 0

        for num in nums:
            res ^= num

        return res


# @leet end
