# @leet start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)

        left = 0
        right = len(chars) - 1

        while left < right:
            if chars[left] > chars[right]:
                chars[left] = chars[right]
            elif chars[left] < chars[right]:
                chars[right] = chars[left]

            left += 1
            right -= 1

        return "".join(chars)


# @leet end
