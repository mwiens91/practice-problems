# @leet start
import math


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # The sum of multiples of x <= n is the sum
        #
        # x + 2x + ... + kx
        #
        # where k == n // x. The sum can be expressed as
        #
        # x + ... + kx = x (1 + ... + k) = x * k * (k + 1) / 2
        #
        # Which is equivalent to x * math.comb(x // n + 1, 2).
        #
        # Let S(x) be the set of numbers <= n. We want to sum the
        # numbers in S(3) ∪ S(5) ∪ S(7). Since these sets are in general
        # not disjoint, we have
        #
        # ∑(S(3) ∪ S(5) ∪ S(7))
        # = ∑(S(3)) + ∑(S(5)) + ∑(S(7))
        #   - ∑(S(3) ∩ S(5)) - ∑(S(3) ∩ S(7)) - ∑(S(5) ∩ S(7))
        #   + ∑(S(3) ∩ S(5) ∩ S(7))
        #
        # (using the inclusion-exclusion principle).
        result = 0

        for coefficient, divisor in [
            (1, 3),
            (1, 5),
            (1, 7),
            (-1, 15),
            (-1, 21),
            (-1, 35),
            (1, 105),
        ]:
            result += coefficient * divisor * math.comb(n // divisor + 1, 2)

        return result


# @leet end
