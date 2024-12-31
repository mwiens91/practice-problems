# @leet start
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)

        return sum(0 if heights[i] == expected[i] else 1 for i in range(len(heights)))


# @leet end
