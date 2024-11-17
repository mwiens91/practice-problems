# @leet start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Idea here: iterate through each number x at index i in the
        # list. For each index i, if x == i or x == n, we move on to the
        # next index; otherwise we swap x into index x and receive a new
        # number y, and we repeat this process. Since each swap moves a
        # number into its correct position, we do at most n swaps. This
        # sorts the list. From there, finding the first missing number
        # is trivial.
        n = len(nums)

        # Swap until sorted
        for i in range(n):
            while nums[i] not in {i, n}:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        # Find first missing number and return it
        i = 0

        while i < n:
            if nums[i] != i:
                break

            i += 1

        return i


# @leet end
