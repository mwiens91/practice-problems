# @leet start
from collections import Counter


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        # Recall each word has exactly two letters. General idea: we'll
        # iterate through the words.
        #
        # - For words which consist of two unique letters, use as many
        # word + complement (the reversed word) pairs as possible.
        #
        # - For words which consist of the same letter twice, we use as
        # many pairs of that word as possible in the palindrome. If
        # there is at least one word with two of the same letter that
        # has an odd frequency count, we can use one of this word in the
        # middle of the palindrome—call this the "leftover middle word".
        word_counts = Counter(words)

        have_leftover_middle_word = False
        num_words_in_palindrome = 0
        unique_letter_words_used_in_palindrome: set[str] = set()

        for word, count in word_counts.items():
            if word[0] != word[1]:
                # Word has two unique letters
                if (
                    word not in unique_letter_words_used_in_palindrome
                    and (complement := word[::-1]) in word_counts
                ):
                    # Process the word and its complement
                    unique_letter_words_used_in_palindrome.update([word, complement])

                    num_words_in_palindrome += 2 * min(count, word_counts[complement])
            else:
                # Word has two repeated letters
                count_is_odd = count % 2 == 1

                if count_is_odd:
                    have_leftover_middle_word = True
                    num_words_in_palindrome += count - 1
                else:
                    num_words_in_palindrome += count

        return 2 * (int(have_leftover_middle_word) + num_words_in_palindrome)


# @leet end
