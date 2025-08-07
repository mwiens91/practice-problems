# @leet start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # Convert to unsigned representation if negative
        if num < 0:
            num &= 0xFFFFFFFF

        result_reversed: list[str] = []

        while num:
            remainder = num % 16

            if remainder >= 10:
                result_reversed.append(chr(ord("a") + remainder - 10))
            else:
                result_reversed.append(str(remainder))

            num //= 16

        return "".join(reversed(result_reversed))


# @leet end
