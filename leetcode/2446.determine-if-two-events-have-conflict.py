# @leet start
class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        def get_minutes_of_day(time_str: str) -> int:
            hours, minutes = map(int, time_str.split(":"))

            return hours * 60 + minutes

        e1_start, e1_end = map(get_minutes_of_day, event1)
        e2_start, e2_end = map(get_minutes_of_day, event2)

        # Return whether there is a non-empty intersection of time
        return e1_start <= e2_end and e1_end >= e2_start


# @leet end
