# @leet start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Define a function to give the XOR of numbers from 0 to n. This
        # is a known result.
        def xor_0_to_n(n: int) -> int:
            match n % 4:
                case 0:
                    return n
                case 1:
                    return 1
                case 2:
                    return n + 1
                case _:
                    # 3
                    return 0

        # We need to find the result of
        #
        # (start + 2 * 0)^(start + 2 * 1)^ ... ^(start + 2 * (n - 1))
        #
        # We can factor each term to get
        #
        # 2 * (start // 2 + i) + (start % 2)
        # = 2 * (start // 2 + i) ^ (start % 2)
        #
        # In the last line either start % 2 = 0, in which case the
        # equality clearly holds since x + 0 = x ^ 0; or start % 2 = 1,
        # in which case the equality holds because adding 1 to an even
        # number is the same as XORing it with 1 (flipping the least
        # significant bit).
        #
        # XORing all these terms together, the result we need to find
        # can be expressed as
        #
        # 2 * ((start // 2 + 0)^...^(start // 2 + n - 1))
        # ^ {n terms of start % 2}
        #
        # The n terms of start % 2 = 0 if start % 2 is 0. If
        # start % 2 is 1, then (start % 2) * (n % 2), because all pairs
        # of start % 2 XORed will cancel each other, leaving at most one
        # remaining.
        #
        # For the result we use the fact that x ^ x = 0 and so the XOR
        # of numbers from (start // 2) to (start // 2  + n - 1) is the
        # same as the XOR of numbers from 0 to (start // 2 - 1) XORed
        # with the XOR of numbers from 0 to (start // 2 + n - 1).
        return 2 * (xor_0_to_n(start // 2 - 1) ^ xor_0_to_n(start // 2 + n - 1)) ^ (
            (start % 2) * (n % 2)
        )


# @leet end
