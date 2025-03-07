# @leet start
class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        # Find the lowest and highest possible difference elements in
        # the copy can have compared to the original
        n = len(original)

        lowest_possible_diff = max(bounds[i][0] - original[i] for i in range(n))
        highest_possible_diff = min(bounds[i][1] - original[i] for i in range(n))

        return max(0, highest_possible_diff - lowest_possible_diff + 1)


# @leet end
