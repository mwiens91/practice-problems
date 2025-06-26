# @leet start
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        val = 1

        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                val *= -1

        return val


# @leet end
