# @leet start
from operator import itemgetter


class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        start_vals = sorted((start, i) for i, (start, _) in enumerate(intervals))
        n = len(start_vals)
        res: list[int] = []

        for _, end in intervals:
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if start_vals[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1

            res.append(start_vals[left][1] if left < n else -1)

        return res


# @leet end
