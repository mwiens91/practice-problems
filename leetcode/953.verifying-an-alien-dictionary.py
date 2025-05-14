# @leet start
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Get position of all letters
        letter_order = {}

        for i, letter in enumerate(order):
            letter_order[letter] = i

        # Return if the words are sorted
        def word_key(word):
            return [letter_order[char] for char in word]

        return all(
            word_key(words[i]) <= word_key(words[i + 1]) for i in range(len(words) - 1)
        )


# @leet end
