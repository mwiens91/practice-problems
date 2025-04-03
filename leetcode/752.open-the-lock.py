# @leet start
from collections import deque
import itertools


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # Transform the target into a tuple of ints
        target_tuple = tuple(map(int, target))

        # Put all deadends in a set as tuples of ints
        deadends_set = {tuple(map(int, deadend)) for deadend in deadends}

        # Edge case: ensure the starting state is not a deadend
        starting_state = (0, 0, 0, 0)

        if starting_state in deadends_set:
            return -1

        # Now do a BFS to find the minimum number of moves to achieve
        # the target. For convenience, add the deadends to the visited
        # set.
        queue: deque[tuple[tuple, int]] = deque([(starting_state, 0)])
        visited = {starting_state} | deadends_set

        while queue:
            # Get current state
            state, num_moves_taken = queue.popleft()

            # Check if we are at the target
            if state == target_tuple:
                return num_moves_taken

            # Visit adjacent states
            for i, delta in itertools.product(range(4), [-1, 1]):
                next_state = state[:i] + ((state[i] + delta) % 10,) + state[i + 1 :]

                if next_state not in visited:
                    queue.append((next_state, num_moves_taken + 1))
                    visited.add(next_state)

        # Impossible to achieve the target
        return -1


# @leet end
