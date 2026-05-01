# @leet start
class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        original = image[sr][sc]

        if color == original:
            return image

        num_rows = len(image)
        num_cols = len(image[0])

        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            row, col = stack.pop()

            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    0 <= row + delta_row < num_rows
                    and 0 <= col + delta_col < num_cols
                    and image[row + delta_row][col + delta_col] == original
                ):
                    image[row + delta_row][col + delta_col] = color

                    stack.append((row + delta_row, col + delta_col))

        return image


# @leet end
