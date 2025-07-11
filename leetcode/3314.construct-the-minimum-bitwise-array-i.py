# @leet start
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        # Define a function that finds the minimal x such that
        # x | (x + 1) == n. I'm not going to prove it here but if n is
        # odd we just unset the least significant bit before the least
        # significant unset bit. For example, suppose n = 55, which has
        # binary representation 110111. Here we take x to have binary
        # representation 110011, so x = 51. Adding 1 to such an x,
        # resets the bit that we unset. If n is even, then there isn't
        # any answer.
        def find_minimal_consecutive_or_component(n: int) -> int:
            if n % 2 == 0:
                return -1

            for bit in range(1, n.bit_length() + 1):
                if n >> bit & 1 == 0:
                    # Unset the first set bit proceeded by an unset bit
                    return n & ~(1 << (bit - 1))

        return list(map(find_minimal_consecutive_or_component, nums))


# @leet end
