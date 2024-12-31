# @leet start
class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> list[list[int]]:
        # Get the maximum distance from the center possible
        max_distance = max(rCenter, rows - 1 - rCenter) + max(
            cCenter, cols - 1 - cCenter
        )

        # Get cells in order of increasing distance
        cell_results = [[rCenter, cCenter]]

        for distance in range(1, max_distance + 1):
            # Get all cells which are a magnitude of distance away. Find
            # the possible rows first, and for each row find
            # corresponding cols.
            cell_rows = range(
                max(0, rCenter - distance), min(rows, rCenter + distance + 1)
            )

            for cell_row in cell_rows:
                # Get the magnitude of the column such that
                # distance = |cell_row - rCenter| + delta_col_magnitude
                col_distance_magnitude = distance - abs(cell_row - rCenter)

                cell_cols = []

                # Add either a single column if the magnitude is 0, or
                # two columns corresponding to adding and subtracting
                # the distance magnitude otherwise
                if col_distance_magnitude == 0:
                    cell_cols.append(cCenter)
                else:
                    if (left_col := cCenter - col_distance_magnitude) >= 0:
                        cell_cols.append(left_col)

                    if (right_col := cCenter + col_distance_magnitude) < cols:
                        cell_cols.append(right_col)

                # Add cells
                cell_results += [[cell_row, cell_col] for cell_col in cell_cols]

        return cell_results


# @leet end
