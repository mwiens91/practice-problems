# @leet start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Look for each character in s in t. If we exhaust t before
        # exhausting s, then s is not a subsequence of t. Otherwise, it
        # is.
        t_idx = 0

        for s_char in s:
            while True:
                # Look for char at current element of t
                try:
                    t_char = t[t_idx]
                except IndexError:
                    # Exhausted t before s
                    return False

                if t_char == s_char:
                    break

                # Try next element of t
                t_idx += 1

            # Set up for next iteration
            t_idx += 1

        return True


# @leet end
