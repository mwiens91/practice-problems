# @leet start
class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        CODE_POINT_LOWER_A = ord("a")
        LINE_MAX_WIDTH = 100

        num_lines = 1
        current_line_width = 0

        for width in [widths[ord(char) - CODE_POINT_LOWER_A] for char in s]:
            if current_line_width + width <= LINE_MAX_WIDTH:
                current_line_width += width
            else:
                num_lines += 1
                current_line_width = width

        return [num_lines, current_line_width]


# @leet end
