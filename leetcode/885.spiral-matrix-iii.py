# @leet start
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        total = rows * cols

        row = rStart
        col = cStart
        result: list[list[int]] = [[row, col]]

        def add_to_result() -> None:
            if 0 <= row < rows and 0 <= col < cols:
                result.append([row, col])

        # Traverse in a spiral pattern and mark down coordinates of the
        # matrix we visit
        step_size = 1

        while len(result) < total:
            # Go right
            for _ in range(step_size):
                col += 1
                add_to_result()

            # Go down
            for _ in range(step_size):
                row += 1
                add_to_result()

            step_size += 1

            # Go left
            for _ in range(step_size):
                col -= 1
                add_to_result()

            # Go up
            for _ in range(step_size):
                row -= 1
                add_to_result()

            step_size += 1

        return result


# @leet end
