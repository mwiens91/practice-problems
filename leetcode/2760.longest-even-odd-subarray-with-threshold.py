# @leet start
class Solution:
    def longestAlternatingSubarray(self, nums: list[int], threshold: int) -> int:
        best_run = 0
        current_run = 0
        current_parity = 0

        for num in nums:
            if num > threshold:
                # Too big, try again at next number
                best_run = max(best_run, current_run)
                current_run = 0
                current_parity = 0
            elif num % 2 != current_parity:
                # Wrong parity, try again at this number
                best_run = max(best_run, current_run)
                current_run = 1 if num % 2 == 0 else 0
                current_parity = 1 if current_run else 0
            else:
                current_run += 1
                current_parity ^= 1

        return max(best_run, current_run)


# @leet end
