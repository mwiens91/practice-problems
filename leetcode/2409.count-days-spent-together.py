# @leet start
import itertools


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        # The number of days in each month, 0-indexed
        NUM_DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Get the number of days that have elapsed at the start of each
        # month
        num_days_elapsed_at_start_of_month = [0] + list(
            itertools.accumulate(NUM_DAYS_IN_MONTH)
        )[:-1]

        # Define a function to convert a date string MM-DD to day of
        # year
        def get_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))

            return num_days_elapsed_at_start_of_month[month - 1] + day

        # Find the starting and ending day of year for the intersection
        # of Alice and Bob's dates
        intersection_start_day_of_year = max(
            get_day_of_year(arriveAlice), get_day_of_year(arriveBob)
        )
        intersection_end_day_of_year = min(
            get_day_of_year(leaveAlice), get_day_of_year(leaveBob)
        )

        return max(0, intersection_end_day_of_year - intersection_start_day_of_year + 1)


# @leet end
