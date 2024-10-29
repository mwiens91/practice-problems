# @leet start
import math

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Go through with a forward iteration. Conceptually, nums is
        # broken up into chunks with separators 0. Within each chunk,
        # we'll keep track of the current maximum and minimum of
        # contiguous numbers we can get a product of.

        # NOTE: I got very close to this on my own, but ultimately
        # needed used Neetcode to figure out exactly how to do this
        current_max = 1
        current_min = 1
        best = -math.inf

        for num in nums:
            # If num == 0 we move onto the next chunk
            if num == 0:
                current_max = 1
                current_min = 1

                best = max(best, 0)

                continue

            # We'll set current max to this after we're done using it
            # for current_min
            new_current_max = max(current_max * num, current_min * num, num)

            current_min = min(current_max * num, current_min * num, num)
            current_max = new_current_max

            best = max(best, current_max)

        return best
# @leet end
