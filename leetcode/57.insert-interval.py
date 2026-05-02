# @leet start
class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        # Starting interval to merge (inclusive)
        left = 0
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][1] >= newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1

        start = left

        # End interval to merge (exclusive)
        left = start
        right = len(intervals) - 1

        while left <= right:
            mid = (left + right) // 2

            if intervals[mid][0] > newInterval[1]:
                right = mid - 1
            else:
                left = mid + 1

        end = left

        # Merge
        merged = (
            [
                min(newInterval[0], intervals[start][0]),
                max(newInterval[1], intervals[end - 1][1]),
            ]
            if start < end
            else newInterval
        )

        return intervals[:start] + [merged] + intervals[end:]


# @leet end
