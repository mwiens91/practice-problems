class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # Use greed. Sort the numbers; the optimized pairings are
        # each even-indexed element with its next element. The maximized
        # sum is thus the sum of all even-indexed elements.
        nums.sort()

        return sum(nums[::2])
