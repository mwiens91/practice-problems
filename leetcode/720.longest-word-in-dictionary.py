# @leet start
class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Sort words in order (1) from shortest to longest and (2)
        # lexicographic
        sorted_words = sorted(words, key=lambda w: (len(w), w))

        # Find what words we can form and keep track of the largest word
        # with the smallest lexicographic order
        precursors = set([""])
        largest_word = ""

        for word in sorted_words:
            if word[:-1] in precursors:
                precursors.add(word)

                if len(word) > len(largest_word):
                    largest_word = word

        return largest_word


# @leet end
