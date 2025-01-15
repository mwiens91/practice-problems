# @leet start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_ints_reversed = [int(x) for x in reversed(num1)]
        num2_ints_reversed = [int(x) for x in reversed(num2)]

        results_len = 1 + max(len(num1_ints_reversed), len(num2_ints_reversed))
        result_ints_reversed = [0] * results_len

        # Add numbers digit by digit
        for i in range(results_len - 1):
            try:
                num_1_digit = num1_ints_reversed[i]
            except IndexError:
                num_1_digit = 0

            try:
                num_2_digit = num2_ints_reversed[i]
            except IndexError:
                num_2_digit = 0

            digit_sum = num_1_digit + num_2_digit

            result_ints_reversed[i] += digit_sum % 10
            result_ints_reversed[i + 1] += digit_sum // 10

        # Remove a possible leading zero from the (not reversed) result
        if result_ints_reversed[-1] == 0:
            result_ints_reversed.pop()

        # Build the string
        return "".join([str(x) for x in reversed(result_ints_reversed)])


# @leet end
