# @leet start
from collections import Counter


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        preferences_count = Counter(students)

        for i, sandwich_type in enumerate(sandwiches):
            if preferences_count[sandwich_type] > 0:
                preferences_count[sandwich_type] -= 1
            else:
                # No one can eat this sandwich
                return len(sandwiches) - i

        # All sandwiches consumed
        return 0


# @leet end
