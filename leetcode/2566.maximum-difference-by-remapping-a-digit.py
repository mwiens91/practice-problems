# @leet start
class Solution:
    def minMaxDifference(self, num: int) -> int:
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

        # For min value, replace all of the first digit with 0
        min_val = int(num_str.replace(num_str[0], "0"))

        return max_val - min_val


# @leet end
