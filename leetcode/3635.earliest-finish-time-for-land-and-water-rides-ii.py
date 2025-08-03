# @leet start
import math


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int],
    ) -> int:
        # NOTE: this is the same solution as 3633. That one has a few
        # comments.
        def find_earliest_finish(
            first_starts: list[int],
            first_durations: list[int],
            second_starts: list[int],
            second_durations: list[int],
        ) -> int:
            earliest_first_finish: float | int = math.inf

            for start, duration in zip(first_starts, first_durations):
                earliest_first_finish = min(earliest_first_finish, start + duration)

            earliest_total_finish = math.inf

            for start, duration in zip(second_starts, second_durations):
                earliest_total_finish = min(
                    earliest_total_finish,
                    max(start, earliest_first_finish) + duration,
                )

            return earliest_total_finish

        return min(
            find_earliest_finish(
                landStartTime, landDuration, waterStartTime, waterDuration
            ),
            find_earliest_finish(
                waterStartTime, waterDuration, landStartTime, landDuration
            ),
        )


# @leet end
