# @leet start
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        has_x = False

        while n >= 10:
            n, rem = divmod(n, 10)

            if rem == x:
                has_x = True

        return n != x and has_x


# @leet end
