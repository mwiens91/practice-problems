# @leet start
import itertools


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        # NOTE: needed ChatGPT's help for the idea of bitmasking DP
        STARTING_SQUARE = 1
        ENDING_SQUARE = 2
        # EMPTY_SQUARE = 0
        OBSTACLE = -1

        num_rows = len(grid)
        num_cols = len(grid[0])

        # Assign each walkable position with an index we'll use in a
        # bitmask. Also find the start position and end position.
        position_bit_idx_dict: dict[tuple[int, int], int] = {}
        bit_idx = 0

        for row, col in itertools.product(range(num_rows), range(num_cols)):
            if (square_type := grid[row][col]) != OBSTACLE:
                if square_type == STARTING_SQUARE:
                    start_position = (row, col)
                elif square_type == ENDING_SQUARE:
                    end_position = (row, col)

                position_bit_idx_dict[(row, col)] = bit_idx
                bit_idx += 1

        # Define a memoized DFS function to return the number of
        # Hamiltonian paths that visit a position (x, y) with a given
        # mask
        memo: dict[tuple[int, int, int], int] = {}
        full_mask = (1 << len(position_bit_idx_dict)) - 1

        def num_valid_paths(x: int, y: int, mask: int) -> int:
            # End position
            if (x, y) == end_position:
                return int(mask == full_mask)

            # Try memo
            if (x, y, mask) in memo:
                return memo[(x, y, mask)]

            # Visit adjacent paths
            result = 0

            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_x = x + dx
                next_y = y + dy

                # If the location is not walkable or is already visited,
                # skip it
                if (
                    next_x,
                    next_y,
                ) not in position_bit_idx_dict or mask >> position_bit_idx_dict[
                    (next_x, next_y)
                ] & 1 == 1:
                    continue

                result += num_valid_paths(
                    next_x,
                    next_y,
                    mask | (1 << position_bit_idx_dict[(next_x, next_y)]),
                )

            # Memoize and return result
            memo[(x, y, mask)] = result

            return result

        return num_valid_paths(
            start_position[0],
            start_position[1],
            1 << position_bit_idx_dict[start_position],
        )


# @leet end
