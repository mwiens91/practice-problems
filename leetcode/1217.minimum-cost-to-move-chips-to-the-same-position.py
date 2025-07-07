# @leet start
class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        # Get the count of chips at even positions and at odd positions
        even_count = 0
        odd_count = 0

        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return min(even_count, odd_count)


# @leet end
