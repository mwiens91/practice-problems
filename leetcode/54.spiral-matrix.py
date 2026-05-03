# @leet start
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res: list[int] = []

        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(matrix[up][i])

            for i in range(up + 1, down + 1):
                res.append(matrix[i][right])

            if left < right and up < down:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[down][i])

                for i in range(down - 1, up, -1):
                    res.append(matrix[i][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return res


# @leet end
