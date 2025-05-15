# @leet start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # The answer is at most 2. We check if s is already a
        # palindrome: if it is we return 1; else return 2.
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return 2

            left += 1
            right -= 1

        return 1


# @leet end
