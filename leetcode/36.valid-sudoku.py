# @leet start
import itertools

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Validate rows
        for i in range(9):
            seen_set = set()

            for j in range(9):
                val = board[i][j]

                if val != "." and val in seen_set:
                    return False

                seen_set.add(val)

        # Validate columns
        for j in range(9):
            seen_set = set()

            for i in range(9):
                val = board[i][j]

                if val != "." and val in seen_set:
                    return False

                seen_set.add(val)

        # Validate sub-boxes
        def validate_subbox(ul_i: int, ul_j: int) -> bool:
            """ul_i is upper left row, ul_j is upper left column."""
            seen_set = set()

            for i, j in itertools.product(range(ul_i, ul_i + 3), range(ul_j, ul_j + 3)):
                val = board[i][j]

                if val != "." and val in seen_set:
                    return False

                seen_set.add(val)

            return True

        for i, j in itertools.product(range(0, 9, 3), range(0, 9, 3)):
            if not validate_subbox(i, j):
                return False

        return True
# @leet end

