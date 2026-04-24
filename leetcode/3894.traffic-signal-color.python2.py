# @leet start
class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """

        if timer == 0:
            return "Green"

        if timer == 30:
            return "Orange"

        if 30 < timer <= 90:
            return "Red"

        return "Invalid"


# @leet end
