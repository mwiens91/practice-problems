# @leet start
class Solution:
    def maximumTime(self, time: str) -> str:
        # Deal with hours and minutes separately
        hours, minutes = time.split(":")

        # Deal with hours for all different cases, setting the maximum
        # time for each
        if hours == "??":
            # Case ??
            hours = "23"
        elif hours[0] == "?":
            # Case ?x
            if int(hours[1]) >= 4:
                # x >= 3
                hours = "1" + hours[1]
            else:
                # x < 3
                hours = "2" + hours[1]
        elif hours[1] == "?":
            # Case x?
            if int(hours[0]) == 2:
                # x == 2
                hours = hours[0] + "3"
            else:
                # x < 2
                hours = hours[0] + "9"

        # Deal with minutes
        if minutes[0] == "?":
            minutes = "5" + minutes[1]

        if minutes[1] == "?":
            minutes = minutes[0] + "9"

        return hours + ":" + minutes


# @leet end
