# @leet start
class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = {"a", "e", "i", "o", "u"}
        right = len(s) - 1

        while right >= 0 and s[right] in VOWELS:
            right -= 1

        return s[: right + 1]


# @leet end
