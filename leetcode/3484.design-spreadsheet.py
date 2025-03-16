# @leet start
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows)]

    def col_letter_to_idx(self, col_letter: str) -> int:
        return ord(col_letter) - ord("A")

    def get_row_and_col_from_cell_reference(
        self, cell_reference: str
    ) -> tuple[int, int]:
        # Recall rows are given to us as 1-indexed, so we need to return
        # them as 0-indexed
        return (int(cell_reference[1:]) - 1, self.col_letter_to_idx(cell_reference[0]))

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.get_row_and_col_from_cell_reference(cell)

        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        summand_strs = formula[1:].split("+")

        # Get values to add
        values = []

        for summand_str in summand_strs:
            if summand_str[0].isalpha():
                # This is a cell reference
                row, col = self.get_row_and_col_from_cell_reference(summand_str)

                values.append(self.sheet[row][col])
            else:
                # It's a literal value
                values.append(int(summand_str))

        # Sum the values
        return sum(values)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @leet end
