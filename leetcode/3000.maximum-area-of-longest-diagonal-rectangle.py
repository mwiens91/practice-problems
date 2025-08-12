# @leet start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        largest_diag = 0  # we'll store the square of the diagonal for simplicity
        area = 0

        for x, y in dimensions:
            diag = x**2 + y**2

            if diag > largest_diag:
                largest_diag = diag
                area = x * y
            elif diag == largest_diag:
                area = max(area, x * y)

        return area


# @leet end
