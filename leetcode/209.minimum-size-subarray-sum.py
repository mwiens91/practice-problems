# @leet start
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Get length of nums
        n = len(nums)

        # Use a sliding window
        min_size_seen = math.inf

        i = 0
        j = -1

        window_sum = 0

        while j < n:
            # Shrink window until its sum is < target
            while window_sum >= target:
                # Update minimum window seen
                min_size_seen = min(min_size_seen, j - i + 1)

                # Move up i
                window_sum -= nums[i]
                i += 1

            # Expand window until its sum is >= target
            while window_sum < target:
                j += 1

                # Exhausted nums
                if j == n:
                    break

                window_sum += nums[j]

        # Return result
        if min_size_seen == math.inf:
            return 0

        return min_size_seen


# @leet end
