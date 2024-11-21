# @leet start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # Get number of rows and columns
        num_rows = len(board)
        num_cols = len(board[0])

        # Get length of word
        word_len = len(word)

        # Define a helper function to get all valid neighbours of a
        # given index
        def get_neighbours(
            row_idx: int, col_idx: int, exclude_set: set[tuple[int, int]]
        ) -> list[tuple[int, int]]:
            neighbours = []

            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                candidate = (row_idx + i, col_idx + j)
                if (
                    0 <= candidate[0] < num_rows
                    and 0 <= candidate[1] < num_cols
                    and candidate not in exclude_set
                ):
                    neighbours.append(candidate)

            return neighbours

        # Recursive function we'll call at each matrix cell that starts
        # with word[0]. word_idx is the index of word the *next* cell
        # needs to test against.
        def recurse(
            row_idx: int, col_idx: int, word_idx: int, exclude_set: set[tuple[int, int]]
        ) -> bool:
            # Base case
            if word_idx == word_len:
                return True

            # Recurse. Find what cells to visit next among valid
            # neighbours (in bounds, not in exclude set)
            valid_neighbours = get_neighbours(row_idx, col_idx, exclude_set)
            next_cells = []

            for neighbour in valid_neighbours:
                if board[neighbour[0]][neighbour[1]] == word[word_idx]:
                    next_cells.append(neighbour)

            # Return True if any of these work
            return any(
                recurse(
                    next_cell[0],
                    next_cell[1],
                    word_idx + 1,
                    exclude_set | {next_cell},
                )
                for next_cell in next_cells
            )

        # Now try each cell
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if board[row_idx][col_idx] == word[0] and recurse(
                    row_idx, col_idx, 1, set([(row_idx, col_idx)])
                ):
                    return True

        return False


# @leet end
