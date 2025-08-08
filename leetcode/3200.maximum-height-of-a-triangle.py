# @leet start
import math


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def get_max_rows(n1: int, n2: int) -> int:
            # - n1 has rows of sizes 1, 3, 5, ...
            # - n2 has rows of sizes 2, 4, 6, ...
            #
            # To get how many rows you can get with these
            # numbers, you need to do a bit of algebra (not
            # included)
            rows_1 = math.isqrt(n1)
            rows_2 = math.floor((math.sqrt(1 + 4 * n2) - 1) / 2)

            if rows_1 <= rows_2:
                return 2 * rows_1

            return 2 * rows_2 + 1

        return get_max_rows(blue, red) if blue >= red else get_max_rows(red, blue)


# @leet end
