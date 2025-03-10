# @leet start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        nums = [int(x) for x in str(n)]

        result = 0

        for i, num in enumerate(nums):
            result += (-1) ** i * num

        return result


# @leet end
