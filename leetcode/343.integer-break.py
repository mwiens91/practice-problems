# @leet start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        if n == 3:
            return 2

        # We want to break n into as many 3s as possible. However if
        # this leaves us with a remainder of 1, it's better to take one
        # less three and get two twos.
        max_num_3s = n // 3

        match n % 3:
            case 0:
                return 3**max_num_3s
            case 1:
                return 3 ** (max_num_3s - 1) * 4
            case _:
                # 2
                return 3**max_num_3s * 2


# @leet end
