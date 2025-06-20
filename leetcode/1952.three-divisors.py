# @leet start
import math


class Solution:
    def isThree(self, n: int) -> bool:
        # A number has exactly three positive divisors iff it is the
        # square of a prime number. (So the divisors are 1, p, and p^2,
        # where p is prime.)
        root = math.isqrt(n)

        # Ensure that the root is an integer and that it is greater than
        # 1
        if root * root != n or root < 2:
            return False

        # Test if the root is prime. There are optimizations you can do
        # here to make this ~2-3x faster, but they don't change the
        # asymptotic complexity.
        for i in range(2, math.isqrt(root) + 1):
            if root % i == 0:
                return False

        return True


# @leet end
