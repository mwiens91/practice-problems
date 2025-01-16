# @leet start
class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        # Sort points by x-value
        points.sort()

        # First ensure all points are distinct
        n = len(points)

        for i in range(n - 1):
            if points[i] == points[i + 1]:
                return False

        # Function to get the slope of two points
        def get_slope(point1: list[int], point2: list[int]) -> float | None:
            delta_y = point2[1] - point1[1]
            delta_x = point2[0] - point1[0]

            try:
                return delta_y / delta_x
            except ZeroDivisionError:
                return None

        # Ensure all slopes are distinct
        first_slope = get_slope(points[0], points[1])

        for i in range(1, n - 1):
            if get_slope(points[i], points[i + 1]) == first_slope:
                return False

        return True


# @leet end
