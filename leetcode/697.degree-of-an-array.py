# @leet start
import math


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # Go through each num in nums, find its count, first index seen,
        # and last index seen
        counts: dict[int, int] = {}
        first_seen_dict: dict[int, int] = {}
        last_seen_dict: dict[int, int] = {}

        for i, num in enumerate(nums):
            # Add to the count
            try:
                counts[num] += 1
            except KeyError:
                # First time seeing this. Add the count and mark the
                # first time we've seen the number.
                counts[num] = 1
                first_seen_dict[num] = i

            # Update the last time we've seen the number
            last_seen_dict[num] = i

        # Find all numbers with the max count
        max_count = max(counts.values())
        numbers_with_max_count = [
            num for num, count in counts.items() if count == max_count
        ]

        # Find the number that results in the shortest subarray with the
        # same degree as the original subarray
        min_subarray_length = math.inf

        for num in numbers_with_max_count:
            min_subarray_length = min(
                min_subarray_length, last_seen_dict[num] - first_seen_dict[num] + 1
            )

        return min_subarray_length


# @leet end
