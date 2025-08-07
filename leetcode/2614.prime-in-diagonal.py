# @leet start
from itertools import chain


class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        # Use fact that all primes >3 are of the form 6k±1
        def is_prime(n: int) -> bool:
            if n == 1:
                return False

            if n <= 3:
                return True

            if n % 2 == 0 or n % 3 == 0:
                return False

            i = 5

            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False

                i += 6

            return True

        n = len(nums)

        return max(
            chain.from_iterable(
                filter(is_prime, [nums[i][i], nums[i][n - 1 - i]]) for i in range(n)
            ),
            default=0,
        )


# @leet end
