# @leet start
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative is always False, zero always true
        if x < 0:
            return False

        if x == 0:
            return True

        # Keep checking that the first digit is the same as the last
        ten_exponent = math.floor(math.log10(x))

        while ten_exponent > 0:
            if math.floor(x / 10**ten_exponent) != x % 10:
                return False

            # Scrap the last and first digit
            x = math.floor(x % 10**ten_exponent / 10)
            ten_exponent -= 2

        return True
# @leet end
