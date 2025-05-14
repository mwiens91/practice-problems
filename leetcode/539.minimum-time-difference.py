# @leet start
import re


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        n = len(timePoints)

        # Transform timestamp into minutes
        minute_points = [0] * n

        for i in range(n):
            hours, minutes = map(int, re.findall(r"\d{2}", timePoints[i]))

            minute_points[i] = hours * 60 + minutes

        # Sort the minute points and find the minimum difference
        minute_points.sort()

        # Initialize the minimum difference with the difference between
        # the smallest and largest number of minutes
        min_diff = 24 * 60 + minute_points[0] - minute_points[-1]

        for i in range(n - 1):
            min_diff = min(min_diff, minute_points[i + 1] - minute_points[i])

        return min_diff


# @leet end
