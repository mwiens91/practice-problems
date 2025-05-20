# @leet start
# pylint: disable=too-many-arguments
class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        # Get area of both rectangles
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        # The the side length of their intersections (or 0 if no
        # intersection) along x and y axes. These formulas are easy to
        # come up with by inspection if you draw out a few examples.
        intersection_x_length = max(min(bx2 - ax1, ax2 - bx1), 0)
        intersection_y_length = max(min(by2 - ay1, ay2 - by1), 0)

        return area_a + area_b - intersection_x_length * intersection_y_length


# @leet end
