# @leet start
class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # NOTE: this solution has a computational complexity of
        # log(n + q log n) where n is the length of nums and q is the
        # size of queries. You can do this solution with a complexitity
        # of log(n + q), but I'm practicing binary searches right now,
        # so that's what I've done here.

        # Find the longest non-overlapping intervals, in order, which
        # are special (each adjacent element has different parity)
        n = len(nums)

        intervals: list[tuple[int, int]] = []

        i = 0

        while i < n:
            # Mark the first index as the start of the interval and find
            # the end index
            start = i

            while i + 1 < n and (nums[i] % 2) != (nums[i + 1] % 2):
                i += 1

            # Add the interval
            intervals.append((start, i))

            # Setup for next iteration
            i += 1

        # For each query, use a binary search to to place the start
        # index of a query into a special interval. (Each start index is
        # guaranteed to lie in exactly one interval.) If the end index
        # of the query also lies in that interval, the query corresponds
        # to a special subarray.
        num_intervals = len(intervals)

        answers: list[bool] = []

        for query_start_idx, query_end_idx in queries:
            left = 0
            right = num_intervals - 1

            while left <= right:
                mid = (left + right) // 2
                mid_interval_start_idx, mid_interval_end_idx = intervals[mid]

                if mid_interval_start_idx <= query_start_idx <= mid_interval_end_idx:
                    break

                if mid_interval_end_idx < query_start_idx:
                    left = mid + 1
                else:
                    right = mid - 1

            # If the query end index lies in the special interval,
            # answer True to the query, otherwise answer False
            answers.append(query_end_idx <= mid_interval_end_idx)

        return answers


# @leet end
