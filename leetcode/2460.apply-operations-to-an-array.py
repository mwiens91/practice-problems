# @leet start
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        # Split result into non-zero and zero parts
        non_zero_res: list[int] = []
        zero_res: list[int] = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            (non_zero_res if nums[i] else zero_res).append(nums[i])

        # Final element
        (non_zero_res if nums[-1] else zero_res).append(nums[-1])

        return non_zero_res + zero_res


# @leet end
