# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx: dict[str, int] = {}

        best = 0
        left = 0

        for right in range(len(s)):
            if s[right] in last_idx:
                left = max(left, last_idx[s[right]] + 1)

            last_idx[s[right]] = right
            best = max(best, right - left + 1)

        return best


# @leet end
