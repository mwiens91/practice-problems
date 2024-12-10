# @leet start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use memoization. This is trivial using combinatorics though (I
        # think?).
        memo: dict[tuple[int, int], int] = {(m - 1, n - 1): 1}

        def num_unique_paths(row: int, col: int) -> int:
            # Lookup previous result
            if (row, col) in memo:
                return memo[(row, col)]

            # Compute result. For num ways we
            num_ways = 0

            if row < m - 1:
                num_ways += num_unique_paths(row + 1, col)

            if col < n - 1:
                num_ways += num_unique_paths(row, col + 1)

            memo[(row, col)] = num_ways

            return num_ways

        # Return the number of unique paths
        return num_unique_paths(0, 0)


# @leet end
