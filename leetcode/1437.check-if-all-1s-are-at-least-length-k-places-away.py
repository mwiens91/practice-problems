# @leet start
import math


class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        # Return True if there are at least k 0s between all 1s, else
        # return False
        last_one_idx = -math.inf

        for i, num in enumerate(nums):
            if num == 1:
                if i - last_one_idx < k + 1:
                    return False

                last_one_idx = i

        return True


# @leet end
