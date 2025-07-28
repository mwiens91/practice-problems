# @leet start
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        proper_divisor_sum = 1

        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                # Both i and num // i divide num
                second_divisor = num // i

                if second_divisor != i:
                    proper_divisor_sum += i + second_divisor
                else:
                    proper_divisor_sum += i

        return num == proper_divisor_sum


# @leet end
