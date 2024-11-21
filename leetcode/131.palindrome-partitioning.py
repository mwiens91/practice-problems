# @leet start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # Defined a memoized function to tell if a string is a
        # palindrome. I'm not actually sure how much memoization
        # benefits us vs hurts us here, but my intuition says better to
        # do it.
        is_palindrome_dict: dict[str, bool] = {}

        def is_palindrome(str_: str) -> bool:
            # All length one strings are palindromes
            n = len(str_)

            if n == 1:
                return True

            # Check if we have the result saved, return it if so
            try:
                return is_palindrome_dict[str_]
            except KeyError:
                pass

            # Find the result
            result = True

            for i in range(n // 2):
                if str_[i] != str_[n - 1 - i]:
                    result = False

                    break

            # Store result and return result
            is_palindrome_dict[str_] = result

            return result

        # We're going to brute force here. Try every valid substring as
        # the first substring, then try every valid substring as the
        # next, etc., until we run out of characters.
        results: list[list[str]] = []

        # Get the length of s
        s_len = len(s)

        def recurse(start_idx: int, prev_substrings: list[str]) -> None:
            # Base case
            if start_idx == s_len:
                results.append(prev_substrings)

                return

            # Recurse—try every possible substring here
            for idx in range(start_idx, s_len):
                this_substring = s[start_idx : idx + 1]

                if is_palindrome(this_substring):
                    recurse(idx + 1, prev_substrings + [this_substring])

        # Get results and return
        recurse(0, [])

        return results


# @leet end
