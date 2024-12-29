# @leet start
class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        # Get dimensions of image
        num_rows = len(image)
        num_cols = len(image[0])

        # Get original color we need to change cells to
        original_color = image[sr][sc]

        # Define a function to change a connected group of the same
        # colors, and define a seen set so we don't reprocess a cell
        seen_set: set[tuple[int, int]] = set()

        def change_connected_colors(row: int, col: int) -> None:
            # Change color
            image[row][col] = color

            # Mark this cell as seen
            seen_set.add((row, col))

            # Visit adjacent cells of same color
            for adj_row, adj_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= adj_row < num_rows
                    and 0 <= adj_col < num_cols
                    and (adj_row, adj_col) not in seen_set
                    and image[adj_row][adj_col] == original_color
                ):
                    change_connected_colors(adj_row, adj_col)

        # Do the flood fill
        change_connected_colors(sr, sc)

        return image


# @leet end
