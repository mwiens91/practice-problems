# @leet start
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        output = []

        for i in range(0, len(nums), 2):
            output += [nums[i + 1]] * nums[i]

        return output


# @leet end
