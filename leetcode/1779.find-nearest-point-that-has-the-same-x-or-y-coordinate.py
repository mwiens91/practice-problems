# @leet start
import math


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_distance = math.inf
        min_distance_idx = -1

        for i, (p_x, p_y) in enumerate(points):
            if p_x == x or p_y == y:
                dist = abs(p_y - y + p_x - x)

                if dist < min_distance:
                    min_distance = dist
                    min_distance_idx = i

        return min_distance_idx


# @leet end
