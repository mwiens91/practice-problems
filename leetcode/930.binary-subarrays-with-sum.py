# @leet start
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # NOTE: Tried a sliding window technique at first. It's way
        # harder than you'd think! Almost got there, then switched to
        # a prefix sum solution, which I also struggled with. I probably
        # could have got it, but was a bit burned out after the sliding
        # window problem solving, so looked at the editorial for the
        # gist.

        # Get prefix sums and their frequency. For each prefix sum, we
        # add to the total subarray count the frequency of prefix sums
        # matching prefix sum - goal: this is the count of distinct
        # indices after which we can start a subarray summing to goal.
        prefix_sum_counts: defaultdict[int, int] = defaultdict(int)

        # We initialize the prefix sum counts with 0 to represent the
        # start of the array
        prefix_sum_counts[0] += 1

        prefix_sum = 0
        total_count = 0

        for num in nums:
            prefix_sum += num

            total_count += prefix_sum_counts[prefix_sum - goal]
            prefix_sum_counts[prefix_sum] += 1

        return total_count


# @leet end
