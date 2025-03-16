# @leet start
from collections import Counter


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        # Make useful sets
        digits_set = set(digits)
        even_digits = set(digit for digit in digits if digit % 2 == 0)
        non_zero_digits = set(digit for digit in digits if digit != 0)

        # Count the number of each digit
        digit_counts = Counter(digits)

        # Count the number of unique even 3-digit numbers
        result_count = 0

        # Iterate over digits in the "hundreds" position
        for hundreds_digit in non_zero_digits:
            # Exclude this digit from being picked again if we've ran out
            tens_excluded_digits = set()

            if digit_counts[hundreds_digit] == 1:
                tens_excluded_digits.add(hundreds_digit)

            # Iterate over digits in the "tens" position
            for tens_digit in digits_set - tens_excluded_digits:
                # Similarly to above, exclude this digit from being
                # picked again if we've ran out
                ones_excluded_digits = tens_excluded_digits.copy()

                if tens_digit == hundreds_digit and digit_counts[tens_digit] == 2:
                    ones_excluded_digits.add(tens_digit)
                elif digit_counts[tens_digit] == 1:
                    ones_excluded_digits.add(tens_digit)

                # Count the number of available even digits to put in
                # the "ones" position
                result_count += len(even_digits - ones_excluded_digits)

        return result_count


# @leet end
