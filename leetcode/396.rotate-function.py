# @leet start
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        curr = 0

        # Set up first value
        for i in range(1, n):
            curr += i * nums[i]

        best = curr

        # Iterate through other vals
        for i in range(n - 1, -1, -1):
            curr += total - n * nums[i]
            best = max(best, curr)

        return best


# @leet end
