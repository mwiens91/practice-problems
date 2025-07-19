# @leet start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        BACKSPACE = "#"

        s_idx = len(s) - 1
        t_idx = len(t) - 1

        # Go through the strings in reverse, comparing indices we don't
        # skip over
        def next_valid_char_idx(s_: str, start_idx: int) -> int:
            skip = 0
            i = start_idx

            while i >= 0:
                if s_[i] == BACKSPACE:
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    break

                i -= 1

            return i

        while True:
            s_idx = next_valid_char_idx(s, s_idx)
            t_idx = next_valid_char_idx(t, t_idx)

            if s_idx < 0 or t_idx < 0:
                return s_idx < 0 and t_idx < 0

            if s[s_idx] != t[t_idx]:
                return False

            s_idx -= 1
            t_idx -= 1


# @leet end
