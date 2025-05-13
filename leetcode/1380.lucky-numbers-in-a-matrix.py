# @leet start
class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row_mins = set(map(min, matrix))
        col_maxes = set(map(max, zip(*matrix)))

        return list(row_mins & col_maxes)


# @leet end
