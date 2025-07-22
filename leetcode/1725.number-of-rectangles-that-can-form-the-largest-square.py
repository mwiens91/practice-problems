# @leet start
class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        max_side_length = 0
        max_side_count = 0

        for l, w in rectangles:
            side_length = min(l, w)

            if side_length > max_side_length:
                max_side_length = side_length
                max_side_count = 1
            elif side_length == max_side_length:
                max_side_count += 1

        return max_side_count


# @leet end
