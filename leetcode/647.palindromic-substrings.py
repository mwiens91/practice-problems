# @leet start
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Go through all possible substrings in increasing order of
        # length and store palindromes based on their start and end
        # index (inclusive)

        # NOTE: not implemented, but we can reduce memory significantly,
        # since for a given length we only need access to palindromes of
        # length - 2
        n = len(s)
        palindrome_idxs = set(
            zip(range(n), range(n))
        )  # all 1-length strings are palindromes

        for length in range(2, n + 1):
            for start_idx in range(n - length + 1):
                # If the letters at the start index and end index are
                # equal and the inner letters are a palindrome, this is
                # also a palindrome
                end_idx = start_idx + length - 1

                if s[start_idx] == s[end_idx] and (
                    length == 2 or (start_idx + 1, end_idx - 1) in palindrome_idxs
                ):
                    palindrome_idxs.add((start_idx, end_idx))

        return len(palindrome_idxs)


# @leet end
