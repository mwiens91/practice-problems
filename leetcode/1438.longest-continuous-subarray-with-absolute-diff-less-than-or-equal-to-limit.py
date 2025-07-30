# @leet start
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        # Use a sliding window and keep track of two monotonic queues:
        # one keeping track of the indices of the smallest elements in
        # the window and one keeping track of the indices of the largest
        # elements
        n = len(nums)

        window_start = 0  # inclusive
        window_end = 1  # exclusive
        longest_window_size = 1

        min_mono_queue = deque([0])
        max_mono_queue = deque([0])

        while window_end < n:
            # Expand window by one
            while min_mono_queue and nums[min_mono_queue[-1]] >= nums[window_end]:
                min_mono_queue.pop()

            min_mono_queue.append(window_end)

            while max_mono_queue and nums[max_mono_queue[-1]] <= nums[window_end]:
                max_mono_queue.pop()

            max_mono_queue.append(window_end)

            window_end += 1

            # Contract the window until the window property is respected
            while nums[max_mono_queue[0]] - nums[min_mono_queue[0]] > limit:
                # For either queue, either window_start is not in the
                # queue or it is the first element
                for queue in [min_mono_queue, max_mono_queue]:
                    if queue[0] == window_start:
                        queue.popleft()

                window_start += 1

            # Update longest window size
            longest_window_size = max(longest_window_size, window_end - window_start)

        return longest_window_size


# @leet end
