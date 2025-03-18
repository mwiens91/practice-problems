# @leet start
from collections import Counter


class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        new_words = [words[0]]

        prev_word_counts = Counter(words[0])

        for word in words[1:]:
            if (word_counts := Counter(word)) == prev_word_counts:
                new_words.append(words[i])

                prev_word_counts = word_counts

        return new_words


# @leet end
