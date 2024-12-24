# @leet start
class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        res = duration

        for i in range(1, len(timeSeries)):
            res += duration + min(0, timeSeries[i] - timeSeries[i - 1] - duration)

        return res


# @leet end
