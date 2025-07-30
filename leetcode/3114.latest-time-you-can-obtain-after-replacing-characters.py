# @leet start
class Solution:
    def findLatestTime(self, s: str) -> str:
        hours, minutes = map(list, s.split(":"))

        if hours[0] == "?":
            hours[0] = "1" if hours[1] == "?" or hours[1] < "2" else "0"

        if hours[1] == "?":
            hours[1] = "1" if hours[0] == "1" else "9"

        if minutes[0] == "?":
            minutes[0] = "5"

        if minutes[1] == "?":
            minutes[1] = "9"

        return "".join(hours) + ":" + "".join(minutes)


# @leet end
