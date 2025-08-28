# @leet start
class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle: list[list[int]] = rectangle
        self.update_history: list[tuple[int, int, int, int, int]] = []

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        self.update_history.append((row1, row2, col1, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for row1, row2, col1, col2, val in reversed(self.update_history):
            if row1 <= row <= row2 and col1 <= col <= col2:
                return val

        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
# @leet end
