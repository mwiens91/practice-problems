# @leet start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Greed: we remove the first occurance of the digit that is
        # proceeded by a number greater than it. If no such first
        # occurance exists, we remove the last occurance of the digit.
        n = len(number)
        last_idx_of_digit: None | int = None

        for i in range(n - 1):
            if number[i] == digit:
                if number[i] < number[i + 1]:
                    return number[:i] + number[i + 1 :]

                last_idx_of_digit = i

        if number[n - 1] == digit:
            last_idx_of_digit = n - 1

        return number[:last_idx_of_digit] + number[last_idx_of_digit + 1 :]


# @leet end
