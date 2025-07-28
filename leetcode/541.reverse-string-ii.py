# @leet start
import math


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s_chars = list(s)

        for i in range(math.ceil(n / (2 * k))):
            left = i * 2 * k
            right = min(i * 2 * k + k - 1, n - 1)

            while left < right:
                s_chars[left], s_chars[right] = s_chars[right], s_chars[left]

                left += 1
                right -= 1

        return "".join(s_chars)


# @leet end
