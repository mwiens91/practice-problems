# @leet start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # We have to shoot the first balloon, so take as many additional
        # balloons as we can when we shoot it. Then for the next
        # remaining balloon, do the same, etc.
        points.sort(key=lambda p: (p[1], p[0]))
        count = 0

        i = 0

        while i < len(points):
            count += 1

            current_end = points[i][1]
            i += 1

            while i < len(points) and points[i][0] <= current_end:
                i += 1

        return count


# @leet end
