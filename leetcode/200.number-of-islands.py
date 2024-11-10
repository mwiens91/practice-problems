# @leet start
from collections import deque
import itertools


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Get grid dimensions
        n = len(grid)
        m = len(grid[0])

        # Convenience function to tell if an index (i, j) is water:
        # either a cell with "0" or out of bounds
        def is_water(i: int, j: int) -> bool:
            # Is this out of bounds?
            if not (0 <= i < n and 0 <= j < m):
                return True

            # Is this "0"?
            if grid[i][j] == "0":
                return True

            # Is "1" (not water)
            return False

        # Initialize a set which holds which indices we've seen
        seen_set = set()

        # Initialize a counter which holds the number of islands we've
        # processed
        counter = 0

        for i, j in itertools.product(range(n), range(m)):
            # Continue if we've already processed the index or if the
            # index contains water
            if (i, j) in seen_set or grid[i][j] == "0":
                continue

            # We've encountered new land here: set up a deque with this
            # index, and add this index to the seen set
            to_process_deque = deque([(i, j)])
            seen_set.add((i, j))

            while to_process_deque:
                # Pop out the head node
                i, j = to_process_deque.pop()

                # Find adjacent land we haven't seen yet
                for idx in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    # If we've already seen the index or it's water,
                    # continue
                    if idx in seen_set or is_water(*idx):
                        continue

                    # Process this later: put back of deque
                    to_process_deque.appendleft(idx)

                    # Mark index as seen
                    seen_set.add(idx)

            counter += 1

        return counter


# @leet end
