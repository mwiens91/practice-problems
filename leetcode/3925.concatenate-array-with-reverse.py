# @leet start
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums.extend(reversed(nums))

        return nums


# @leet end
