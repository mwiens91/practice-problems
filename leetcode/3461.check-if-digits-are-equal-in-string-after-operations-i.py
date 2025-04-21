# @leet start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))

        for _ in range(len(digits) - 2):
            new_digits: list[int] = []

            for first, second in zip(digits, digits[1:]):
                new_digits.append((first + second) % 10)

            digits = new_digits

        return digits[0] == digits[1]


# @leet end
