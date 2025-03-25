# @leet start
class Solution:
    def checkValidCuts(
        self, n: int, rectangles: list[list[int]]  # pylint: disable=unused-argument
    ) -> bool:
        # Define a function that merges a number of possibly overlapping
        # intervals and then counts the number of "cuts" merged
        # intervals. A cut is defined to be a point that has the
        # following properties:
        #
        # - the cut is between 1 and n - 1
        # - the cut is not an interior point in any interval
        # - the space between any two cut contains an interval
        #
        # For the purposes of this problem, two intervals are not
        # considered to be overlapping if one starts immediately after
        # another ends, so intervals are only merged when the start
        # point of an interval lies between the start point of another
        # interval (inclusive) and the end point of another interval
        # (exclusive).
        def get_num_cuts(intervals: list[tuple[int, int]]) -> int:
            # Sort the intervals based on start index (and then end
            # index, although this isn't useful here)
            intervals.sort()

            # Go through intervals, counting the number of cuts
            num_cuts = 0

            current_interval_start, current_interval_end = intervals[0]

            for interval_start, interval_end in intervals[1:]:
                # Extend the current interval if there's overlap, else
                # count a cut and start a new interval.
                if current_interval_start <= interval_start < current_interval_end:
                    current_interval_end = max(current_interval_end, interval_end)
                else:
                    num_cuts += 1

                    current_interval_start = interval_start
                    current_interval_end = interval_end

            return num_cuts

        # For each rectangle, record the interval of space they take up
        # along both axes
        x_intervals: list[tuple[int, int]] = []
        y_intervals: list[tuple[int, int]] = []

        for start_x, start_y, end_x, end_y in rectangles:
            x_intervals.append((start_x, end_x))
            y_intervals.append((start_y, end_y))

        # Return whether there are at least two spaces on either x or y
        # axes where we can make two "cuts"
        return get_num_cuts(x_intervals) >= 2 or get_num_cuts(y_intervals) >= 2


# @leet end
