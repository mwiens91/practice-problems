# @leet start
from math import comb


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Use math result
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]


# @leet end
