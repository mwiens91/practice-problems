# @leet start
import itertools


class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        # The number of days in each month, 0-indexed
        NUM_DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Get the prefix sum of the number of days that have elapsed at
        # the start of a month, again 0-indexed
        num_days_elapsed_at_beginning_of_month = [0] + list(
            itertools.accumulate(NUM_DAYS_IN_MONTH)
        )[:-1]

        # Define a function to get the number of days that have elapsed
        # since the start of the year given a date MM-DD
        def get_number_of_days_elapsed(date_str: str) -> int:
            month, day = date_str.split("-")
            
            return num_days_elapsed_at_beginning_of_month[month - 1] + day

        return 5


# @leet end

