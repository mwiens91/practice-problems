# @leet start
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        n = len(colors)

        left_color = colors[-1]
        num_groups = 0

        for i, color in enumerate(colors):
            # Get the right colour
            right_color = colors[(i + 1) % n]

            # Add an alternating group if this colour is different from
            # its adjacent tiles
            if color not in {left_color, right_color}:
                num_groups += 1

            # Set left colour to current colour for next iteration
            left_color = color

        return num_groups


# @leet end
