# @leet start
class Solution:
    def convertToBase7(self, num: int) -> str:
        # Edge case: num == 0
        if num == 0:
            return "0"

        # Store sign and work with the absolute value of the number
        if num < 0:
            num = abs(num)
            sign = "-"
        else:
            sign = ""

        # Find the base 7 representation
        base_7_digit_chars_reversed: list[str] = []

        while num:
            base_7_digit_chars_reversed.append(str(num % 7))
            num //= 7

        return sign + "".join(reversed(base_7_digit_chars_reversed))


# @leet end
