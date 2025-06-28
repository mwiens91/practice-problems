# @leet start
class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        return sum(
            1 for start, end in zip(startTime, endTime) if start <= queryTime <= end
        )


# @leet end
