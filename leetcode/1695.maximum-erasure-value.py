# @leet start
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        # Use a sliding window
        n = len(nums)

        start = 0  # inclusive
        end = 0  # exclusive

        nums_in_window: set[int] = set()
        window_sum = 0
        best = 0

        while end < n:
            # Expand window
            while end < n and nums[end] not in nums_in_window:
                window_sum += nums[end]
                nums_in_window.add(nums[end])
                end += 1

            # Update max
            best = max(best, window_sum)

            # Contract window
            while end < n and nums[end] in nums_in_window:
                window_sum -= nums[start]
                nums_in_window.remove(nums[start])
                start += 1

        return best


# @leet end
