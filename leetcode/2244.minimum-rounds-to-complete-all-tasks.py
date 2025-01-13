# @leet start
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        # Get counts of all the tasks
        counts = Counter(tasks)

        # For each task level, find the number of rounds it takes to
        # finish all tasks
        rounds = 0

        for count in counts.values():
            # If any counts are 1, there is no solution
            if count == 1:
                return -1

            # Try to do as many groups of three as possible
            rounds += count // 3

            # Find remaining number of tasks. If the remainder is 1, we
            # need to convert one of the previous groups of 3 to a group
            # of 2 and add another group of 2. If the remainder is 2, we
            # need to add another group of 2. In either case, we add
            # another round
            if count % 3:
                rounds += 1

        return rounds


# @leet end
