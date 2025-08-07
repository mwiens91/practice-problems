# @leet start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1

        while n:
            if n & 1 == prev:
                return False

            prev = n & 1
            n >>= 1

        return True


# @leet end
