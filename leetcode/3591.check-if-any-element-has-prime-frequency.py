# @leet start
from collections import Counter


class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        def is_prime(n: int) -> bool:
            # We can make this more efficient by using the fact that all
            # primes > 3 have form 6k ± 1. We check all possible prime
            # divisors.
            if n <= 1:
                return False

            if n <= 3:
                # n == 2 or n == 3
                return True

            if n % 2 == 0 or n % 3 == 0:
                return False

            i = 5

            while i * i < n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False

                i += 6

            return True

        return any(is_prime(freq) for freq in Counter(nums).values())


# @leet end
