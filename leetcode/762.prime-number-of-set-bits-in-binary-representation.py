# @leet start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # NOTE: we could be more efficient in counting bits by
        # reusing previous results or looping in a clever way,
        # but for this problem's constraints it isn't worth it.
        # Honestly there's probably even a constant time solution.
        PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}

        def has_prime_set_bits(n: int) -> bool:
            set_bits_count = 0

            while n:
                if n & 1:
                    set_bits_count += 1

                n >>= 1

            return set_bits_count in PRIMES

        return sum(1 for n in range(left, right + 1) if has_prime_set_bits(n))


# @leet end
