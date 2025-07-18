# @leet start
class Solution:
    def isValid(self, word: str) -> bool:
        LOWER_VOWELS = {"a", "e", "o", "i", "u"}

        if len(word) < 3:
            return False

        seen_vowel = False
        seen_cons = False

        for char in word:
            if char.isalpha():
                if char.lower() in LOWER_VOWELS:
                    seen_vowel = True
                else:
                    seen_cons = True
            elif not char.isdigit():
                return False

        return seen_vowel and seen_cons


# @leet end
