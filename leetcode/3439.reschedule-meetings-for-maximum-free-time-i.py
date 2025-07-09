# @leet start
class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: list[int], endTime: list[int]
    ) -> int:
        # Get the gaps in events where no meetings occur
        gaps = (
            [startTime[0]]
            + [
                start_next - end_prev
                for start_next, end_prev in zip(startTime[1:], endTime)
            ]
            + [eventTime - endTime[-1]]
        )

        # We can move k events, which lets us combine k + 1 gaps. Find
        # the maximum run of k + 1 gaps.
        n = len(gaps)
        current_run = sum(gaps[: k + 1])
        best_run = current_run

        for i in range(k + 1, n):
            current_run -= gaps[i - k - 1]
            current_run += gaps[i]

            best_run = max(best_run, current_run)

        return best_run


# @leet end
