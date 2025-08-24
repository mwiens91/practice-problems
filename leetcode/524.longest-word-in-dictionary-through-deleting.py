# @leet start
from string import ascii_lowercase


class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # Create a 2D array where jump_table[i][c] gives the next
        # index j>=i where c appears in s. If no index exists, it's
        # marked as -1.
        n = len(s)

        char_to_idx = {c: ord(c) - ord("a") for c in ascii_lowercase}
        jump_table_reversed: list[list[int]] = []
        next_table_entry = [-1] * 26  # this variable is always safe to modify

        for i in range(n - 1, -1, -1):
            next_table_entry[char_to_idx[s[i]]] = i
            jump_table_reversed.append(next_table_entry[:])

        jump_table = jump_table_reversed[::-1]

        # Find the longest word in the dictionary that is a subsequence
        # of s
        longest_word = ""

        for word in dictionary:
            if len(word) < len(longest_word):
                # Don't bother if this is shorter than a word we've
                # already matched
                continue

            i = 0

            for char in word:
                if i >= n:
                    break

                # Find next index where the char occurs
                i = jump_table[i][char_to_idx[char]]

                if i == -1:
                    break

                i += 1
            else:
                # Word is a match
                if len(word) > len(longest_word):
                    longest_word = word
                else:
                    # len(word) == len(longest_word)
                    longest_word = min(longest_word, word)

        return longest_word


# @leet end
