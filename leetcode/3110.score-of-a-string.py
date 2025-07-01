# @leet start
class Solution:
    def scoreOfString(self, s: str) -> int:
        s_code_points = list(map(ord, s))

        score = 0

        for code_point, next_code_point in zip(s_code_points, s_code_points[1:]):
            score += abs(code_point - next_code_point)

        return score


# @leet end
