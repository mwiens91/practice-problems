# @leet start
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        num_rows = len(rowSum)
        num_cols = len(colSum)

        result = [[0] * num_cols for _ in range(num_rows)]

        # We'll fill up column capacities from left to right, so we'll
        # keep track of the first column we haven't yet filled up to
        # save a tiny bit of time
        start_col_idx = 0

        for i in range(num_rows):
            for j in range(start_col_idx, num_cols):
                start_col_idx = j

                transfer = min(rowSum[i], colSum[j])

                result[i][j] = transfer
                rowSum[i] -= transfer
                colSum[j] -= transfer

                if not rowSum[i]:
                    break

        return result


# @leet end
