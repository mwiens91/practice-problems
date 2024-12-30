# @leet start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Find maximum congiguous subarray of length k
        current_sum = 0

        # Get first length k sum
        for i in range(k):
            current_sum += nums[i]

        maximum_sum = current_sum

        # Get all length k sums
        n = len(nums)

        for i in range(k, n):
            current_sum -= nums[i - k]
            current_sum += nums[i]

            maximum_sum = max(maximum_sum, current_sum)

        # Return best average
        return maximum_sum / k


# @leet end
