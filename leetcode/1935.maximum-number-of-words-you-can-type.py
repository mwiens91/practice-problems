# @leet start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Find the count of typable words
        count = 0
        broken_letters_set = set(brokenLetters)

        for word in text.split():
            if not any(letter in broken_letters_set for letter in word):
                count += 1

        return count


# @leet end
