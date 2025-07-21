# @leet start
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        n_temp = n

        while n_temp:
            digit = n_temp % 10

            digit_sum += digit
            digit_prod *= digit

            n_temp //= 10

        return n % (digit_sum + digit_prod) == 0


# @leet end
