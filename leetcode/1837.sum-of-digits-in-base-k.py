# @leet start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits_sum = 0

        while n:
            # Get this iteration's digit and add it to the sum
            digits_sum += n % k

            # Set up for next iteration's digit
            n //= k

        return digits_sum


# @leet end
