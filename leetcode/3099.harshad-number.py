# @leet start
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = sum(map(int, str(x)))

        if x % sum_of_digits == 0:
            return sum_of_digits

        return -1


# @leet end
