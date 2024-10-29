# @leet start
import math

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Go through with a forward iteration, resetting current
        # cumulative sum each time the previous cumulative sum was
        # negative
        cum_sum = -math.inf
        best_cum_sum = -math.inf

        for num in nums:
            cum_sum = max(cum_sum, 0)
            cum_sum += num

            best_cum_sum = max(best_cum_sum, cum_sum)

        return best_cum_sum
# @leet end
