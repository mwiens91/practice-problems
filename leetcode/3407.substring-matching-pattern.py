# @leet start
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # NOTE: this commented out solution is (probably) going to be
        # faster, but I want to try to do this in a "basic" way
        #
        # import re
        # return bool(re.search(p, s))

        # Get the start and end part of p such that
        # p_start + "*" + p_end = p
        p_start, p_end = p.split("*")
        n_s = len(s)

        start_range_end = n_s - len(p_start) - len(p_end) + 1

        for i in range(start_range_end):
            if all(s[i + j] == p_start[j] for j in range(len(p_start))):
                end_min_idx = i + len(p_start)
                break
        else:
            # Couldn't match the start of the pattern
            return False

        end_range_end = n_s - len(p_end) + 1

        for i in range(end_min_idx, end_range_end):
            if all(s[i + j] == p_end[j] for j in range(len(p_end))):
                return True

        return False


# @leet end
