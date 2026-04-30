# @leet start
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        suffixMaxes = [nums[-1]] * len(nums)

        # Dont need two first suffixes and already included the last
        for i in range(len(nums) - 2, 1, -1):
            suffixMaxes[i] = max(nums[i], suffixMaxes[i + 1])

        prefixMax = nums[0]
        ans = [nums[0]]

        for i in range(1, len(nums)):
            if (
                i == len(nums) - 1
                or nums[i] > suffixMaxes[i + 1]
                or nums[i] > prefixMax
            ):
                ans.append(nums[i])

            prefixMax = max(nums[i], prefixMax)

        return ans


# @leet end
