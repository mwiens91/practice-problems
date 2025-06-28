# @leet start
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            # Test if word is a palindrome
            left = 0
            right = len(word) - 1

            while left < right:
                if word[left] != word[right]:
                    break

                left += 1
                right -= 1
            else:
                return word

        return ""


# @leet end
