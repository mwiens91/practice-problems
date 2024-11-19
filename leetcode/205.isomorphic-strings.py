# @leet start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # It'll be easiest to explain here with an example:
        # suppose s = paper and t = title. We'll have assign codes such
        # that for s,
        #
        # p -> 1, a -> 2, e -> 3, r -> 4;
        #
        # and for t,
        #
        # t -> 1, i -> 2, l -> 3, r -> 4.
        #
        # So we assign codes based on some count. When we encounter a
        # character we've seen before, we ensure the "s code" and "t
        # code" is the same.
        count = 0

        s_codes = {}
        t_codes = {}

        for s_ch, t_ch in zip(s, t):
            if s_ch not in s_codes and t_ch not in t_codes:
                # Add code
                s_codes[s_ch] = count
                t_codes[t_ch] = count

                count += 1
            else:
                # Try to match
                try:
                    assert s_codes[s_ch] == t_codes[t_ch]
                except (KeyError, AssertionError):
                    return False

        return True


# @leet end
