# @leet start
from operator import itemgetter


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=itemgetter(0))

        res: list[list[int]] = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                res.append(curr)
                curr = intervals[i]

        res.append(curr)

        return res


# @leet end
