# @leet start
class Solution:
    def maxProduct(self, words: list[str]) -> int:
        # Turn each word into a bitmask that tells us whether a
        # character is present in the word
        n = len(words)
        word_masks: list[int] = [0] * n

        for i, word in enumerate(words):
            for char in word:
                word_masks[i] |= 1 << (ord(char) - ord("a"))

        # Find the pair maximizing len(word1) * len(word2) where word1
        # and word2 share no common letters
        max_value = 0

        for i in range(n):
            for j in range(i + 1, n):
                if word_masks[i] & word_masks[j] == 0:
                    max_value = max(max_value, len(words[i]) * len(words[j]))

        return max_value


# @leet end
