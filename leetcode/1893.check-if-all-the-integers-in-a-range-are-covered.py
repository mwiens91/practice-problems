# @leet start
class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        # Sort intervals by start, then end
        ranges.sort()

        # Extend the coverage from left to right. The coverage end
        # variable below is *non-inclusive* (important!).
        coverage_end = left

        for start, end in ranges:
            if start > coverage_end:
                return False

            coverage_end = max(coverage_end, end + 1)

            if coverage_end > right:
                return True

        return False


# @leet end
