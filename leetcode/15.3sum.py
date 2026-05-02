# @leet start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []

        n = len(nums)
        i = 0

        while i < n - 2 and nums[i] <= 0:
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            i += 1

            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1

        return res


# @leet end
