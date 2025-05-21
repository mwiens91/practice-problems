# @leet start
class Solution:
    def reverseBits(self, n: int) -> int:
        NUM_BITS = 32

        result = 0

        for _ in range(NUM_BITS):
            result = (result << 1) | n & 1
            n >>= 1

        return result


# @leet end
