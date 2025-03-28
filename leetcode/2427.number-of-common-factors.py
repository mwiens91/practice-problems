# @leet start
import math


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        greatest_common_divisor = math.gcd(a, b)

        # The number of common factors of a and b is equal to the number
        # of elements that divide the greatest common divisor
        return 1 + sum(
            1
            for x in range(1, greatest_common_divisor)
            if greatest_common_divisor % x == 0
        )


# @leet end
