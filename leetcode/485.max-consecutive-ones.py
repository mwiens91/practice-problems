# @leet start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best_run = 0
        current_run = 0

        for num in nums:
            if num == 1:
                current_run += 1
                best_run = max(best_run, current_run)
            else:
                current_run = 0

        return best_run


# @leet end
