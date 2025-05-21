# @leet start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Iterate through prefix sums while maintaining a dictionary
        # containing prefix sum frequencies. For each index j,
        #
        # - if the prefix_sum[j] == k, we increment the count of
        # subarrays with sum equal to k
        # - for each i < j where prefix_sum[i] == prefix_sum[j] - k, we
        # increment the count of subarrays with sum equal to k
        #
        # We can merge the first case into the second by initializing
        # the prefix sum frequency of 0 to a count of 1 to account for
        # the first case in which subarrays starting from the beginning
        # of the array, effectively adding prefix_sum[-1] = 0.
        prefix_sum_freqs: defaultdict[int, int] = defaultdict(int)
        prefix_sum_freqs[0] += 1

        prefix_sum = 0
        subarrays_with_k_sum = 0

        for num in nums:
            prefix_sum += num

            subarrays_with_k_sum += prefix_sum_freqs[prefix_sum - k]

            prefix_sum_freqs[prefix_sum] += 1

        return subarrays_with_k_sum


# @leet end
