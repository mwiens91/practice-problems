# @leet start
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        # Whitespace
        while i < n and s[i] == " ":
            i += 1

        # Sign
        sign = 1

        if i < n and s[i] in {"-", "+"}:
            if s[i] == "-":
                sign = -1

            i += 1

        start = i

        # Digits
        while i < n and s[i].isdigit():
            i += 1

        return min(max(sign * int(s[start:i]) if start < i else 0, -(2**31)), 2**31 - 1)


# @leet end
