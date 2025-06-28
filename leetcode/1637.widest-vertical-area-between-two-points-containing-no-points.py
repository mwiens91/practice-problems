# @leet start
class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()

        max_distance = 0

        for (prev_x, _), (x, _) in zip(points, points[1:]):
            max_distance = max(max_distance, x - prev_x)

        return max_distance


# @leet end
