# @leet start
import itertools


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Number of strings passed in
        n_strings = len(strs)

        # Find longest prefix string
        longest_prefix = ""

        str_idx = 0

        # For this loop, we keep iterating until we find a character
        # that is not common at a given index, or until we exhaust the
        # shortest string
        try:
            while True:
                common_char = strs[0][str_idx]

                # Test if all strings have the same character at str_idx
                for str_ in itertools.islice(strs, 1, n_strings):
                    assert str_[str_idx] == common_char

                # Update
                str_idx += 1
                longest_prefix += common_char

        except (AssertionError, IndexError):
            pass

        return longest_prefix


# @leet end
