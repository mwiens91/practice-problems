# @leet start
class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # For max value, find first non-9 digit and replace all of that
        # digit with 9
        for digit in num_str:
            if digit != "9":
                max_val = int(num_str.replace(digit, "9"))

                break
        else:
            # All digits 9
            max_val = num

        # For min value, if the first digit is non-1, set all of that
        # digit to 1; if it is 1, find the first non-0 and 1 digit and
        # set all of that digit to 0.
        if num_str[0] != "1":
            min_val_replacement_digit = "1"
        else:
            min_val_replacement_digit = "0"

        for digit in num_str:
            if digit not in {"0", "1"}:
                min_val = int(num_str.replace(digit, min_val_replacement_digit))

                break
        else:
            # Leading digit is 1 and all other digits 0 or 1
            min_val = num

        return max_val - min_val


# @leet end
