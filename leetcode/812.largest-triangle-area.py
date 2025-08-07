# @leet start
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        # NOTE: This should be done with a "convex hull" type
        # algorithm. I'm not doing that here, because I don't
        # want to (re-)learn it and the constraints don't
        # justify using it, but just making a note of it here.
        largest_area = 0

        # Brute force all areas with the "shoelace formula"
        for comb in combinations(points, 3):
            area = 0

            for i in range(3):
                area += (
                    comb[i][0] * comb[(i + 1) % 3][1]
                    - comb[(i + 1) % 3][0] * comb[i][1]
                )

            area = 0.5 * abs(area)

            largest_area = max(largest_area, area)

        return largest_area


# @leet end
