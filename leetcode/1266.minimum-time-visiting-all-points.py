# @leet start
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time_taken = 0
        x, y = points[0]

        for next_x, next_y in points[1:]:
            # We go diagonally until we achieve the minimum needed
            # vertical or horizontal displacment: this takes
            # min(delta_x, delta_y) seconds. Then we go straight: this
            # takes max(delta_x, delta_y) - min(delta_x, delta_y)
            # seconds.
            time_taken += max(abs(next_x - x), abs(next_y - y))

            x = next_x
            y = next_y

        return time_taken


# @leet end
