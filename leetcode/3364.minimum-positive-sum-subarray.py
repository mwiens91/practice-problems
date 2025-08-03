# @leet start
import itertools
import math


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        prefix_sums = [0] + list(itertools.accumulate(nums))

        # For each end index we'll iterate over start indices and find
        # the minimum positive sum subarray
        min_pos_subarray_sum = math.inf
        end_idx = l - 1

        while end_idx < n:
            for start_idx in range(max(0, end_idx - r + 1), end_idx - l + 2):
                subarray_sum = prefix_sums[end_idx + 1] - prefix_sums[start_idx]

                if subarray_sum > 0:
                    min_pos_subarray_sum = min(min_pos_subarray_sum, subarray_sum)

            end_idx += 1

        return min_pos_subarray_sum if min_pos_subarray_sum < math.inf else -1


# @leet end
