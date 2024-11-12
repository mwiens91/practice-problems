# @leet start
class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        # Sort all arrays by starting time
        startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))

        # Define recursive function to determine the max profit starting
        # from a given job index. We'll make an array to store the best
        # profit for each job that we've already calculated so we don't
        # do repeated work.
        n = len(startTime)

        max_profit_memo = [0] * n

        # This is a helper function to help find the next available job
        # after a given job index
        def find_next_available_job_idx(job_idx: int) -> int | None:
            this_end_time = endTime[job_idx]

            # Do a binary search
            start = job_idx + 1
            end = n - 1

            while start < end:
                mid = (start + end) // 2

                mid_start_time = startTime[mid]

                if this_end_time <= mid_start_time:
                    end = mid
                else:
                    start = mid + 1

            # If the end time is greater than all starting times, this
            # loop will end with start == end == n - 1. Thus we don't
            # know whether the n - 1 index job is actually available or
            # not at this point, so we gotta check. If it isn't, we
            # return None.
            if start == n - 1:
                if this_end_time <= startTime[n - 1]:
                    return n - 1

                # No available jobs
                return None

            # For start != n - 1, return the next available job
            return start

        def get_max_profit(job_idx: int = 0) -> int:
            # Try getting a memoized solution
            if max_profit := max_profit_memo[job_idx]:
                return max_profit

            # Find next available job
            next_available_job_idx = find_next_available_job_idx(job_idx)

            # Get max profit. Three cases: if we're at the last job
            # index, we use the profit for the current job; if there is
            # no next available job but we're not at the last job index,
            # we compare (1) the profit for the current job with (2) the
            # max profit of the next job index; otherwise, we compare
            # (1) the profit for the current job combined with the max
            # profit obtained from taking the next available job with
            # (2) the max profit of the next job index.
            if job_idx == n - 1:
                max_profit = profit[job_idx]
            elif next_available_job_idx is None:
                max_profit = max(
                    profit[job_idx],
                    get_max_profit(job_idx + 1),
                )
            else:
                max_profit = max(
                    profit[job_idx] + get_max_profit(next_available_job_idx),
                    get_max_profit(job_idx + 1),
                )

            # Memoize the solution
            max_profit_memo[job_idx] = max_profit

            return max_profit

        # Find the max profit
        return get_max_profit()


# @leet end
