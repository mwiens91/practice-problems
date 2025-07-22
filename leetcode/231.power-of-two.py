# @leet start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n ^ (1 << (n.bit_length() - 1)) == 0


# @leet end
