# @leet start
import re


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()

        # Convert day and month to required format
        day = day[:-2].zfill(2)

        match month:
            case "Jan":
                month = "01"
            case "Feb":
                month = "02"
            case "Mar":
                month = "03"
            case "Apr":
                month = "04"
            case "May":
                month = "05"
            case "Jun":
                month = "06"
            case "Jul":
                month = "07"
            case "Aug":
                month = "08"
            case "Sep":
                month = "09"
            case "Oct":
                month = "10"
            case "Nov":
                month = "11"
            case _:
                month = "12"

        return "-".join((year, month, date))


# @leet end
