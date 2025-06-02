# @leet start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        # Go through all characters in s. For characters in the first
        # half, increment counts of vowels. For characters in the second
        # half, decrement counts of vowels.
        start_of_second_half = len(s) // 2
        vowel_counts = 0

        for i, char in enumerate(s):
            if char in VOWELS:
                vowel_counts += 1 if i < start_of_second_half else -1

        # If the first half contains the same vowels as the second half,
        # the vowel counts will be 0
        return vowel_counts == 0


# @leet end
