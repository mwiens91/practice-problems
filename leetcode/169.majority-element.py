# @leet start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        curr = nums[0]
        count = 0

        for num in nums:
            if num == curr:
                count += 1
            elif count:
                count -= 1
            else:
                curr = num
                count = 1

        return curr


# @leet end
