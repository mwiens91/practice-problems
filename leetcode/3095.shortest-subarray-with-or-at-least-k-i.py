# @leet start
import math


class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        # Handle edge case
        if k == 0:
            return 1

        MAX_BITS = 6

        # For each bit position, count how many times it has been set in
        # a window
        n = len(nums)
        window_start = 0
        window_end = 0
        window_or = 0
        bit_set_counter = [0] * MAX_BITS

        shortest_length = math.inf

        while window_end < n:
            # Expand window until the OR of the window is >=k if
            # possible
            while window_or < k and window_end < n:
                num = nums[window_end]

                i = 0

                while num:
                    if num & 1:
                        bit_set_counter[i] += 1
                        window_or |= 1 << i

                    num >>= 1
                    i += 1

                window_end += 1

            # Contract window until the OR is <k
            while window_or >= k:
                shortest_length = min(shortest_length, window_end - window_start)

                num = nums[window_start]

                i = 0

                while num:
                    if num & 1:
                        bit_set_counter[i] -= 1

                        if bit_set_counter[i] == 0:
                            window_or &= ~(1 << i)

                    num >>= 1
                    i += 1

                window_start += 1

        return shortest_length if shortest_length < math.inf else -1


# @leet end
