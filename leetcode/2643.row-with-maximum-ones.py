# @leet start
class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        most_ones = 0
        idx_with_most_ones = 0

        for i, row in enumerate(mat):
            if (ones_count := row.count(1)) > most_ones:
                most_ones = ones_count
                idx_with_most_ones = i

        return [idx_with_most_ones, most_ones]


# @leet end
