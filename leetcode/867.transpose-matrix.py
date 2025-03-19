# @leet start
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [list(tup) for tup in zip(*matrix)]


# @leet end
