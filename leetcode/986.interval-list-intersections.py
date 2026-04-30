# @leet start
class Solution:
    def intervalIntersection(
        self, firstList: list[list[int]], secondList: list[list[int]]
    ) -> list[list[int]]:
        ans: list[list[int]] = []

        firstIdx = 0
        secondIdx = 0

        while firstIdx < len(firstList) and secondIdx < len(secondList):
            inter_start = max(firstList[firstIdx][0], secondList[secondIdx][0])
            inter_end = min(firstList[firstIdx][1], secondList[secondIdx][1])

            if inter_start <= inter_end:
                ans.append([inter_start, inter_end])

            # Move up on whichever list's current interval end first
            if firstList[firstIdx][1] < secondList[secondIdx][1]:
                firstIdx += 1
            else:
                secondIdx += 1

        return ans


# @leet end
