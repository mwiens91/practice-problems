# @leet start
class Solution:
    def countPoints(
        self, points: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        answer = [0] * len(queries)

        for i, (x, y, r) in enumerate(queries):
            r_sqrd = r**2

            for x_p, y_p in points:
                if (x_p - x) ** 2 + (y_p - y) ** 2 <= r_sqrd:
                    answer[i] += 1

        return answer


# @leet end
