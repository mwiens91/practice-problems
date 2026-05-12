# @leet start
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0

        curr_color = "-1"
        curr_max = 0

        for color, val in zip(colors, neededTime):
            res += val

            if color == curr_color:
                curr_max = max(curr_max, val)
            else:
                res -= curr_max

                curr_color = color
                curr_max = val

        return res - curr_max


# @leet end
