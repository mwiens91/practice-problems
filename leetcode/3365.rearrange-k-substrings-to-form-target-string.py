# @leet start
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        # If the string length is not divisible by k, this is not
        # possible
        n = len(s)

        if n % k != 0:
            return False

        # First split s into k equal length substrs and keep track of
        # their counts
        counts = {}

        substr_len = n // k
        loop_index_range = list(range(0, n - substr_len + 1, substr_len))

        for i in loop_index_range:
            s_substr = s[i : i + substr_len]

            try:
                counts[s_substr] += 1
            except KeyError:
                counts[s_substr] = 1

        # Now see if we can from t using these substrs
        for i in loop_index_range:
            t_substr = t[i : i + substr_len]

            try:
                assert counts[t_substr] > 0
            except (AssertionError, KeyError):
                # Can't make t from s substrs
                return False

            counts[t_substr] -= 1

        return True


# @leet end
