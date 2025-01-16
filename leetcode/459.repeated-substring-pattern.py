# @leet start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Try each substring whose length divides the string length
        for substr_end_idx in range(1, n // 2 + 1):
            if (
                n % substr_end_idx == 0
                and s[:substr_end_idx] * (n // substr_end_idx) == s
            ):
                return True

        return False


# @leet end
