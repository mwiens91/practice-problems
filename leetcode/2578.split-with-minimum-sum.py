# @leet start
class Solution:
    def splitNum(self, num: int) -> int:
        num1_digits: list[str] = []
        num2_digits: list[str] = []

        # Assign sorted digits to num1 and num2
        for i, digit in enumerate(sorted(str(num))):
            if i % 2 == 0:
                num1_digits.append(digit)
            else:
                num2_digits.append(digit)

        # Find the sum of the split digits
        return int("".join(num1_digits)) + int("".join(num2_digits))


# @leet end
