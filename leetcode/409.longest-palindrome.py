# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts: dict[str, int] = {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        odd = 0
        pairs = 0

        for count in counts.values():
            pairs += count // 2
            odd |= count % 2

        return pairs * 2 + odd


# @leet end
