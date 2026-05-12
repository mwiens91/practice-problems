# @leet start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0

        prod = 1
        left = 0

        for i, num in enumerate(nums):
            prod *= num

            while left <= i and prod >= k:
                prod //= nums[left]
                left += 1

            res += i - left + 1

        return res


# @leet end
