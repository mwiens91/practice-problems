# @leet start
class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        prev_char: None | str = None

        run_start_idx = 0
        run_length = 0

        large_group_intervals: list[list[int]] = []

        for i, char in enumerate(s):
            if char != prev_char:
                # End of group started/continued with previous
                # character. Add interval if group is large.
                if run_length >= 3:
                    large_group_intervals.append([run_start_idx, i - 1])

                # Reset run
                prev_char = char
                run_start_idx = i
                run_length = 1
            else:
                run_length += 1

        # Possibly add final group
        if run_length >= 3:
            large_group_intervals.append([run_start_idx, len(s) - 1])

        return large_group_intervals


# @leet end
