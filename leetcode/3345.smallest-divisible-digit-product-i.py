# @leet start
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            n_remaining = n
            digit_prod = 1

            while n_remaining and digit_prod:
                digit_prod *= n_remaining % 10
                n_remaining //= 10

            if digit_prod % t == 0:
                return n

            n += 1


# @leet end
