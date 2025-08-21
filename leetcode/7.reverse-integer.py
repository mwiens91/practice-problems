# @leet start
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        result = 0

        while x:
            result = result * 10 + x % 10

            if result > MAX_INT + 1 or sign == 1 and result > MAX_INT:
                return 0

            x //= 10

        return sign * result


# @leet end
