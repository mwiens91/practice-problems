# @leet start
import itertools
import math
import statistics


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        num_rows = len(img)
        num_cols = len(img[0])

        new_img = [[0] * num_cols for _ in range(num_rows)]

        # Use these row and column index deltas to get values for
        # elements in a given element's box
        box_idx_deltas = list(itertools.product(range(-1, 2), range(-1, 2)))

        # Smooth each element
        for row, col in itertools.product(range(num_rows), range(num_cols)):
            nums_in_box = []

            for delta_row, delta_col in box_idx_deltas:
                if (
                    0 <= (target_row := row + delta_row) < num_rows
                    and 0 <= (target_col := col + delta_col) < num_cols
                ):
                    nums_in_box.append(img[target_row][target_col])

            new_img[row][col] = math.floor(statistics.fmean(nums_in_box))

        return new_img


# @leet end
