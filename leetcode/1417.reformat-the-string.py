# @leet start
import itertools


class Solution:
    def reformat(self, s: str) -> str:
        # Separate numeric and alphabetic characters
        alpha = []
        numeric = []

        for char in s:
            if char.isalpha():
                alpha.append(char)
            else:
                numeric.append(char)

        # Get out if one list is longer by more than one character
        num_alpha = len(alpha)
        num_numeric = len(numeric)

        if abs(num_alpha - num_numeric) > 1:
            return ""

        # Build a valid permutation and return it
        longer_list, shorter_list = (
            (alpha, numeric) if num_alpha >= num_numeric else (numeric, alpha)
        )
        permutation_char_list = []

        for char1, char2 in itertools.zip_longest(longer_list, shorter_list):
            permutation_char_list.append(char1)

            if char2 is not None:
                permutation_char_list.append(char2)

        return "".join(permutation_char_list)


# @leet end
