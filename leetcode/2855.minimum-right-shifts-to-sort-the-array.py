# @leet start
class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        # Find pivot index i where nums[i - 1] > nums[i] (include i = 0,
        # comparing last and first indices). If there are multiple pivot
        # indices, we return -1, since in that case no shift will result
        # in a sorted list.
        n = len(nums)
        pivot: None | int = None

        for i in range(n):
            if nums[i - 1] > nums[i]:
                if pivot is not None:
                    return -1

                pivot = i

        # If pivot is 0 or None (which occurs only when n = 1), no
        # shifts are required
        return 0 if not pivot else n - pivot


# @leet end
