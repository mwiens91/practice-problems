# @leet start
class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        good_numbers_sum = 0

        n = len(nums)

        for i, num in enumerate(nums):
            # Add to good numbers sum if the number is greater than its
            # left and right neighbours (provided they exist)
            if (i - k < 0 or nums[i - k] < num) and (i + k >= n or nums[i + k] < num):
                good_numbers_sum += num

        return good_numbers_sum


# @leet end
