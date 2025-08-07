# @leet start
class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        n = len(nums)

        for i, num in enumerate(nums):
            if num == 1:
                one_idx = i
            elif num == n:
                n_idx = i

        return one_idx + n - 1 - n_idx - (1 if n_idx < one_idx else 0)


# @leet end
