# @leet start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # We're doing this pseudo-base-26 expansion
        #
        # xn * 26**n + ... + x1 * 26**1 + x0 * 26**0
        #
        # where we restrict 1 <= xi <= 26. It's a little weird, but we
        # can treat it similarly to a normal base-26 expansion except
        # that we need to handle the case when xi == 26.
        #
        # There are probably better ways of describing this
        # problem. It's a little odd and hard to wrap my brain around.
        CODE_POINT_A = ord("A")

        result_chars_reversed: list[str] = []

        while columnNumber > 0:
            this_char = chr(CODE_POINT_A + (columnNumber - 1) % 26)

            result_chars_reversed.append(this_char)

            columnNumber //= 26

            if this_char == "Z":
                columnNumber -= 1

        return "".join(reversed(result_chars_reversed))


# @leet end
