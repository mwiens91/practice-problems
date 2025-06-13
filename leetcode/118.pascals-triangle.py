# @leet start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = [[1]]

        for _ in range(1, numRows):
            # Construct the current row
            prev_row = triangle[-1]
            current_row = [1]

            for i in range(len(prev_row) - 1):
                current_row.append(prev_row[i] + prev_row[i + 1])

            current_row.append(1)

            # Set up for next row
            triangle.append(current_row)

        return triangle


# @leet end
