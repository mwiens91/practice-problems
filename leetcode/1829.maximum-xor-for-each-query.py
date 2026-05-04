# @leet start
class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        n = len(nums)
        res = [0] * n
        max_num = 2**maximumBit - 1

        xor = 0

        for i, num in enumerate(nums):
            xor ^= num
            res[n - 1 - i] = xor ^ max_num

        return res


# @leet end
