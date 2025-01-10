# @leet start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        # Build up the result string. We'll build it up in reverse and
        # then flip it after
        reverse_result = []

        count_to_two = 0

        for char in reversed(str(n)):
            reverse_result.append(char)

            if count_to_two == 2:
                reverse_result.append(".")

            count_to_two = (count_to_two + 1) % 3

        # Remove final "." if the number of chars in the string
        # representation of n is an exact multiple of 3
        if reverse_result[-1] == ".":
            reverse_result.pop()

        return "".join(reversed(reverse_result))


# @leet end
