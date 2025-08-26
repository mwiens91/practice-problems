# @leet start
import statistics


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        waiting_times: list[int] = []

        next_available = 0

        for arrival, duration in customers:
            next_available = max(next_available, arrival) + duration
            waiting_times.append(next_available - arrival)

        return statistics.fmean(waiting_times)


# @leet end
