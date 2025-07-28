# @leet start
class Solution:
    def isUgly(self, n: int) -> bool:
        ALLOWED_PRIME_FACTORS = {2, 3, 5}

        if n < 1:
            return False

        for prime in ALLOWED_PRIME_FACTORS:
            while n % prime == 0:
                n //= prime

        return n == 1


# @leet end
