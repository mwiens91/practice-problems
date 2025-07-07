# @leet start
from datetime import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        DATE_FORMAT = "%Y-%m-%d"

        return abs(
            (
                datetime.strptime(date1, DATE_FORMAT)
                - datetime.strptime(date2, DATE_FORMAT)
            ).days
        )


# @leet end
