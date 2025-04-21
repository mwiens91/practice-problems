# @leet start
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        # If there are positive elements in the list, sum the positive
        # elements and return them. Else, return the least negative
        # number.
        max_num = max(nums)

        if max_num > 0:
            return sum(num for num in set(nums) if num > 0)

        return max_num


# @leet end
