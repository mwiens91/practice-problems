# @leet start
class Solution:
    def countTime(self, time: str) -> int:
        hours, minutes = time.split(":")

        if hours[0] == hours[1] == "?":
            hours_options = 24
        elif hours[0] == "?":
            hours_options = 3 if hours[1] <= "3" else 2
        elif hours[1] == "?":
            hours_options = 10 if hours[0] <= "1" else 4
        else:
            hours_options = 1

        minutes_options = 1

        if minutes[0] == "?":
            minutes_options *= 6

        if minutes[1] == "?":
            minutes_options *= 10

        return hours_options * minutes_options


# @leet end
