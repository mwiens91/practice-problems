# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize res[i] to store the product of the last n - 1 - i
        # numbers
        res = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            res[i] = nums[i + 1] * res[i + 1]

        # Products except self
        prefix_prod = nums[0]

        for i in range(1, len(nums)):
            res[i] *= prefix_prod
            prefix_prod *= nums[i]

        return res


# @leet end
