# @leet start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_valid(start_idx: int, end_idx: int, have_deleted: bool = False) -> bool:
            # Base case
            if start_idx >= end_idx:
                return True

            # Current pair is valid. Recurse.
            if s[start_idx] == s[end_idx]:
                return is_valid(start_idx + 1, end_idx - 1, have_deleted)

            # Current pair is invalid. If we haven't deleted already try
            # skipping either index and then recursing.
            if not have_deleted:
                return is_valid(start_idx + 1, end_idx, True) or is_valid(
                    start_idx, end_idx - 1, True
                )

            return False

        return is_valid(0, len(s) - 1)


# @leet end
