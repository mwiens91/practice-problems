# @leet start
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        NOT_VISITED = -1
        rows = len(mat)
        cols = len(mat[0])

        layer: list[tuple[int, int]] = []
        res = [[NOT_VISITED for _ in range(cols)] for _ in range(rows)]

        # Put zero cells in a list
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    layer.append((row, col))
                    res[row][col] = 0

        # Do multi-source BFS
        dist = 0

        while layer:
            next_layer: list[tuple[int, int]] = []
            dist += 1

            for row, col in layer:
                for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    adj_row = row + delta_row
                    adj_col = col + delta_col

                    if (
                        0 <= adj_row < rows
                        and 0 <= adj_col < cols
                        and res[adj_row][adj_col] == NOT_VISITED
                    ):
                        next_layer.append((adj_row, adj_col))
                        res[adj_row][adj_col] = dist

            layer = next_layer

        return res


# @leet end
