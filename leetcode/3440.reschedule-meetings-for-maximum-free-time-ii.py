# @leet start
from itertools import accumulate


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        n = len(startTime)

        # Get the n meeting lengths and the n + 1 gaps in between
        # meetings
        meetings = [end - start for start, end in zip(startTime, endTime)]
        gaps = (
            [startTime[0]]
            + [
                start_next - end_prev
                for start_next, end_prev in zip(startTime[1:], endTime)
            ]
            + [eventTime - endTime[-1]]
        )

        # Now for each meeting with index i, we try (1) moving it into a
        # non-adjacent gap if possible (gap indices < i or > i + 1), (2)
        # shifting it within an adjacent gap (gap indices i or i + 1)
        gap_prefix_maxes = list(accumulate(gaps, max))
        gap_suffix_maxes = list(accumulate(gaps[::-1], max))[::-1]

        best_free_time = 0

        for i, meeting_length in enumerate(meetings):
            if (
                i >= 1
                and meeting_length <= gap_prefix_maxes[i - 1]
                or i <= n - 2
                and meeting_length <= gap_suffix_maxes[i + 2]
            ):
                best_free_time = max(
                    best_free_time, gaps[i] + meeting_length + gaps[i + 1]
                )
            else:
                best_free_time = max(best_free_time, gaps[i] + gaps[i + 1])

        return best_free_time


# @leet end
