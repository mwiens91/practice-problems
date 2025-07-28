# @leet start
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits)

        i = 0

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        # If the last bit is part of a two-bit character starting at n -
        # 2, we skip ahead to i = n. Otherwise the last two indices are
        # one-bit characters.
        return i == n - 1


# @leet end
