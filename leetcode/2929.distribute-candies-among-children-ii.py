# @leet start
import math


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # NOTE: This is identical to my solution to LC 2928. I explain
        # this solution there.
        result = 0

        for m in range(4):
            sign = (-1) ** m
            num_intersections_with_size_m = math.comb(3, m)

            superset_size = n - m * (limit + 1) + 2

            if superset_size > 0:
                result += (
                    sign * num_intersections_with_size_m * math.comb(superset_size, 2)
                )
            else:
                break

        return result


# @leet end
