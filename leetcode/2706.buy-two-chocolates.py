# @leet start
import heapq


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        leftover = money - sum(heapq.nsmallest(2, prices))

        return leftover if leftover >= 0 else money


# @leet end
