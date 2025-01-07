# @leet start
class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = [int(x) for x in str(num)]

        # Try finding the first 6 and changing it to a 9
        try:
            first_6_idx = digits.index(6)
            digits[first_6_idx] = 9
        except ValueError:
            pass

        # Return the maximum 69 number
        return int("".join([str(x) for x in digits]))


# @leet end
