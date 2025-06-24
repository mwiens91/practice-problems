# @leet start
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        # Get intervals of num indices that appear in the final result
        n = len(nums)
        intervals: list[list[int]] = []

        for i, num in enumerate(nums):
            if num == key:
                # Either extend the previous interval or start a new one
                interval_start = max(0, i - k)
                interval_end = min(n - 1, i + k)

                if intervals and intervals[-1][1] >= interval_start:
                    intervals[-1][1] = interval_end
                else:
                    intervals.append([interval_start, interval_end])

        return [i for start, end in intervals for i in range(start, end + 1)]


# @leet end
