# @leet start
from itertools import zip_longest


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        k_list = list(map(int, str(k)))

        # Do manual arithmetic with carry from right to left
        result_reversed: list[int] = []
        carry = 0

        for num_digit, k_digit in zip_longest(
            reversed(num), reversed(k_list), fillvalue=0
        ):
            digit_sum = num_digit + k_digit + carry

            result_reversed.append(digit_sum % 10)
            carry = digit_sum // 10

        if carry:
            result_reversed.append(carry)

        return list(reversed(result_reversed))


# @leet end
