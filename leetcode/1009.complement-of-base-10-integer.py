# @leet start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = (1 << max(n.bit_length(), 1)) - 1

        return ~n & mask


# @leet end
