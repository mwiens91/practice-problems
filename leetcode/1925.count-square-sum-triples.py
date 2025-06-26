# @leet start
import math


class Solution:
    def countTriples(self, n: int) -> int:
        # There's a mathy way to do this that I'm not implementing here:
        # look up "primitive Pythagorean triple generator algorithm";
        # that algorithm needs to be modified and you need to do a bit
        # of extra work on the side to get all triples, but it is more
        # efficient. I'm just doing brute force here.
        count = 0

        for b in range(1, n):
            for a in range(1, b):
                # Test a < b
                c_squared = a * a + b * b
                c_root_floor = math.isqrt(c_squared)

                if c_root_floor > n:
                    break

                if c_root_floor * c_root_floor == c_squared:
                    # Count both (a, b, c) and (b, a, c)
                    count += 2
            else:
                # Test a == b
                c_squared = 2 * b * b
                c_root_floor = math.isqrt(c_squared)

                if c_root_floor <= n and c_root_floor * c_root_floor == c_squared:
                    # Count (b, b, c)
                    count += 1

        return count


# @leet end
