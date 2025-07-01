# @leet start
class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            num_str = str(num)
            result += int(max(num_str) * len(num_str))

        return result


# @leet end
