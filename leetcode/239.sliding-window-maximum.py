# @leet start
from itertools import islice
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # NOTE: Using monotonically decreasing queue idea from Neetcode video.
        # I did not come up with the idea on my own.

        # Set up deque and solution array
        nums_len = len(nums)
        solution = [0] * (nums_len - k + 1)

        max_deque = deque([nums[0]])

        # Define functions to process element leaving window and element
        # entering window. Look up monotonically decreasing queue to
        # understand what's happening here.
        def process_leaving(x):
            if x == max_deque[0]:
                max_deque.popleft()

        def process_entering(x):
            while max_deque and x > max_deque[-1]:
                max_deque.pop()

            max_deque.append(x)

        # Look at first k-length window
        for num in islice(nums, 1, k):
            process_entering(num)

        solution[0] = max_deque[0]

        # Look at the remaining k-length windows
        for i in range(1, nums_len - k + 1):
            process_leaving(nums[i - 1])
            process_entering(nums[i + k - 1])

            solution[i] = max_deque[0]

        return solution
# @leet end
