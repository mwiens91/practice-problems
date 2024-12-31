# @leet start
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # Function to get slope from coordinates i and i + 1
        def get_slope(i: int) -> float | None:
            delta_y = coordinates[i + 1][1] - coordinates[i][1]
            delta_x = coordinates[i + 1][0] - coordinates[i][0]

            return None if delta_x == 0 else delta_y / delta_x

        # Get slope from first pair of coordinates
        slope = get_slope(0)

        # Ensure all other coordinate pairs generate same slope
        for i in range(1, len(coordinates) - 1):
            if get_slope(i) != slope:
                return False

        return True


# @leet end
