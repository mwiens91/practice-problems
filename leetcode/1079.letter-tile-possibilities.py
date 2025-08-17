# @leet start
from collections import Counter
from collections.abc import Iterator
from math import factorial, prod


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Suppose we have distinct values x_1, ..., x_n with
        # multiplicities m_1, ..., m_n. The number of distinct k-length
        # sequences we can make is the sum over all possible
        # combinations of 0 <= t_i <= m_i such that sum(t_i) = k of
        #
        # k! / prod(t_i!)
        mults = list(Counter(tiles).values())  # mult is shorthand for multiplicities
        num_mults = len(mults)

        # NOTE: ChatGPT helped me a lot with coming up with and
        # understanding the following function
        def get_mult_combinations(
            mult_idx: int, remaining: int
        ) -> Iterator[tuple[int, ...]]:
            # If we're at the last multiplicity index, complete the
            # combination if possible
            if mult_idx == num_mults - 1:
                if 0 <= remaining <= mults[mult_idx]:
                    yield (remaining,)
                return

            # Yield a combination using each possible amount i of this
            # multiplicity
            for i in range(mults[mult_idx] + 1):
                for tail in get_mult_combinations(mult_idx + 1, remaining - i):
                    yield (i,) + tail

        result = 0

        for k in range(1, len(tiles) + 1):
            k_factorial = factorial(k)

            for comb in get_mult_combinations(0, k):
                result += k_factorial // prod(map(factorial, comb))

        return result


# @leet end
