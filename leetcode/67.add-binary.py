# @leet start
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = list(map(int, a))
        b_list = list(map(int, b))

        # Iterate from most significant digit to least and form result
        # in reverse order
        result_reversed: list[int] = []
        carry = 0

        for a_digit, b_digit in zip_longest(
            reversed(a_list), reversed(b_list), fillvalue=0
        ):
            digit_sum = a_digit + b_digit + carry

            result_reversed.append(digit_sum % 2)
            carry = digit_sum // 2

        # If there's still a carry, add it to the list
        if carry:
            result_reversed.append(carry)

        return "".join(map(str, reversed(result_reversed)))


# @leet end
