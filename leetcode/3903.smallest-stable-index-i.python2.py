# @leet start
class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        mins = [nums[n - 1]] * n

        for i in range(n - 2, -1, -1):
            mins[i] = min(nums[i], mins[i + 1])

        curr_max = nums[0]

        for i, num in enumerate(nums):
            curr_max = max(curr_max, num)

            if curr_max - mins[i] <= k:
                return i

        return -1


# @leet end
