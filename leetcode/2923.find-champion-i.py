# @leet start
class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                # If a team is stronger than all other teams (except
                # itself), it's the champion
                if col == 0 and i != j:
                    break
            else:
                return i


# @leet end
