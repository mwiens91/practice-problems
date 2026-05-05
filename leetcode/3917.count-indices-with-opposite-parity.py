# @leet start
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        odd_count = 0
        even_count = 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 == 0:
                nums[i] = odd_count
                even_count += 1
            else:
                nums[i] = even_count
                odd_count += 1

        return nums


# @leet end
