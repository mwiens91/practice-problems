# @leet start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort the input by increasing starting time
        intervals.sort()

        # Store the current interval and all merged intervals
        current_start, current_end = intervals[0]
        merged_intervals = []

        for this_start, this_end in intervals:
            if this_start <= current_end:
                # Overlap, so merge
                current_end = max(current_end, this_end)
            else:
                # No overlap, store old and start new interval
                merged_intervals.append([current_start, current_end])

                current_start = this_start
                current_end = this_end

        # Store the final interval
        merged_intervals.append([current_start, current_end])

        return merged_intervals


# @leet end
