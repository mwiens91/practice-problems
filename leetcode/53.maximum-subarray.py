# @leet start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[-1]
        curr = 0

        for val in nums:
            curr = max(curr, 0)
            curr += val
            best = max(best, curr)

        return best


# @leet end
