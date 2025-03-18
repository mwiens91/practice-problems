# @leet start
class Solution:
    def largestInteger(self, num: int) -> int:
        # Get even and odd digits and sort them in descending order
        digits = [int(x) for x in str(num)]

        even_digits = sorted((x for x in digits if x % 2 == 0), reverse=True)
        odd_digits = sorted((x for x in digits if x % 2 == 1), reverse=True)

        # Form the new number
        even_iter = iter(even_digits)
        odd_iter = iter(odd_digits)

        new_num_digits = [
            next(even_iter) if x % 2 == 0 else next(odd_iter) for x in digits
        ]

        return int("".join([str(x) for x in new_num_digits]))


# @leet end
