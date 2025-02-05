# @leet start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Make a set containing lower- and upper-case vowels
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        # Since strings are immutable we need to work with a list of chars
        chars = list(s)

        # Swap all vowels
        left = 0
        right = len(chars) - 1

        while left < right:
            # Move the left and right pointers to the nearest vowel
            while left < right and chars[left] not in vowels:
                left += 1

            while left < right and chars[right] not in vowels:
                right -= 1

            # Swap the vowels
            chars[left], chars[right] = chars[right], chars[left]

            # Set up for next iteration
            left += 1
            right -= 1

        return "".join(chars)


# @leet end
