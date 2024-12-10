# @leet start
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Get number of rows
        n = len(triangle)

        # Use memoization
        memo: dict[tuple[int, int], int] = {}

        def min_path(row: int, col: int) -> int:
            # Get stored result
            if (row, col) in memo:
                return memo[(row, col)]

            # Compute result
            res = triangle[row][col]

            if row < n - 1:
                res += min(min_path(row + 1, col), min_path(row + 1, col + 1))

            memo[row, col] = res

            return res

        return min_path(0, 0)


# @leet end
