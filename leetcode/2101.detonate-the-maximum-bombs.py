# @leet start
class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        # Translate this to a graph problem. Make a dictionary of edges
        # by comparing all pairs of bombs. There *might* be an
        # optimization here by sorting the bombs in some clever way; I'm
        # just going to go for the O(n^2) time construction for now.
        num_bombs = len(bombs)

        edge_dict: dict[int, list[int]] = {
            bomb_idx: [] for bomb_idx in range(num_bombs)
        }

        for first_bomb_idx in range(num_bombs):
            first_bomb_x, first_bomb_y, first_bomb_radius = bombs[first_bomb_idx]

            for second_bomb_idx in range(first_bomb_idx + 1, num_bombs):
                second_bomb_x, second_bomb_y, second_bomb_radius = bombs[
                    second_bomb_idx
                ]

                # Get distance between bombs
                delta_x_squared = (first_bomb_x - second_bomb_x) ** 2
                delta_y_squared = (first_bomb_y - second_bomb_y) ** 2

                distance_between_bombs_squared = delta_x_squared + delta_y_squared

                # See if bomb 1 can detonate bomb 2 and vice versa
                if first_bomb_radius**2 >= distance_between_bombs_squared:
                    edge_dict[first_bomb_idx].append(second_bomb_idx)

                if second_bomb_radius**2 >= distance_between_bombs_squared:
                    edge_dict[second_bomb_idx].append(first_bomb_idx)

        # Next, we'll run a depth first search on each bomb. We'll skip
        # starting a DFS on a bomb we've already processed as part of
        # another DFS. Beyond that we can't really reuse results in a
        # trivial way because the graph is in general cyclic.
        max_bombs = 0

        bomb_idxs_processed: set[int] = set()  # reset this set each DFS

        def find_num_bombs_detonated(bomb_idx: int) -> int:
            # If we've already detonated this bomb, it doesn't count
            if bomb_idx in bomb_idxs_processed:
                return 0

            # Mark this bomb as processed
            bomb_idxs_processed.add(bomb_idx)

            # Count number of bombs detonated as a result of detonating
            # this bomb, including this one
            bombs_detonated = 1

            for child_idx in edge_dict[bomb_idx]:
                bombs_detonated += find_num_bombs_detonated(child_idx)

            return bombs_detonated

        # Find maximum number of bombs we can detonate. We'll add all
        # bombs we process over all DFSs in here
        bomb_idxs_visited: set[int] = set()

        for bomb_idx in range(num_bombs):
            if bomb_idx not in bomb_idxs_visited:
                # Update max bombs
                max_bombs = max(max_bombs, find_num_bombs_detonated(bomb_idx))

                # Add to the visited set and reset the processed set
                bomb_idxs_visited |= bomb_idxs_processed
                bomb_idxs_processed = set()

        return max_bombs


# @leet end
