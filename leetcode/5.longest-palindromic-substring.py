# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        best_left = 0
        best_right = 0

        for i in range(1, n):
            for left, right in ((i - 1, i), (i, i)):
                while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1

                left += 1
                right -= 1

                if right - left > best_right - best_left:
                    best_left = left
                    best_right = right

        return s[best_left : best_right + 1]


# @leet end
