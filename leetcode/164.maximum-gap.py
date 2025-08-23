# @leet start
import math


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        # NOTE: Needed ChatGPT for hints
        n = len(nums)

        if len(nums) == 1:
            return 0

        max_num = max(nums)
        min_num = min(nums)

        if max_num == min_num:
            return 0

        # The maximum gap must be at least
        #
        # Δ = ceiling((max - min) / (n - 1)),
        #
        # so we can partition the numbers into buckets with this
        # width and compare across buckets. The ith bucket contains
        # elements in the half-open range
        #
        # [min + i * Δ, min + (i + 1) * Δ).
        #
        # Note that the last bucket is either empty or contains only the
        # max. In terms of code we only need to keep track of the
        # minimum and maximum of each bucket.
        delta = math.ceil((max_num - min_num) / (n - 1))
        buckets: list[list[int]] = [
            [] for _ in range(n)
        ]  # each bucket is empty or contains [min_bucket, max_bucket]

        for num in nums:
            bucket_idx = (num - min_num) // delta

            if buckets[bucket_idx]:
                if num < buckets[bucket_idx][0]:
                    buckets[bucket_idx][0] = num
                elif num > buckets[bucket_idx][1]:
                    buckets[bucket_idx][1] = num
            else:
                buckets[bucket_idx] = [num, num]

        # Find the maximum gap: which will always occur in adjacent
        # numbers between buckets
        max_gap = 0
        current_start = buckets[0][1]

        for bucket in buckets[1:]:
            if bucket:
                max_gap = max(max_gap, bucket[0] - current_start)
                current_start = bucket[1]

        return max_gap


# @leet end
