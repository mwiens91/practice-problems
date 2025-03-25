# @leet start
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        # Sort the meetings in ascending order by start day first, then
        # end day
        sorted_meetings = sorted(meetings, key=lambda x: (x[0], x[1]))

        # Count the number of days spent in meetings. Since meetings can
        # overlap, we build up the longest interval of days when we
        # encounter overlapping meetings. If meetings don't overlap, we
        # start new intervals.
        days_in_meetings = 0

        interval_start_day, interval_end_day = sorted_meetings[0]

        for meeting_start_day, meeting_end_day in sorted_meetings[1:]:
            # If this meeting overlaps the current interval, extend the
            # current interval (if possible). Otherwise, count the
            # current interval and start a new one.
            if interval_start_day <= meeting_start_day <= interval_end_day:
                interval_end_day = max(interval_end_day, meeting_end_day)
            else:
                days_in_meetings += interval_end_day - interval_start_day + 1

                interval_start_day = meeting_start_day
                interval_end_day = meeting_end_day

        # Count the final interval
        days_in_meetings += interval_end_day - interval_start_day + 1

        # Return the number of days not in meetings
        return days - days_in_meetings


# @leet end
