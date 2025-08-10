# @leet start
class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                prefix_sum += nums[i]
            else:
                break

        # Return largest number greater than or equal to the prefix sum
        # not present in nums
        nums_set = set(nums)

        while prefix_sum in nums_set:
            prefix_sum += 1

        return prefix_sum


# @leet end
