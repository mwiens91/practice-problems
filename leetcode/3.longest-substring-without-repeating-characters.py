# @leet start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx: dict[str, int] = {}

        best = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in last_idx:
                left = max(left, last_idx[ch] + 1)

            last_idx[ch] = right
            best = max(best, right - left + 1)

        return best


# @leet end
