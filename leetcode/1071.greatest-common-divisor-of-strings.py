# @leet start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # First get the longest common prefix, by finding the ending
        # index (exclusive)
        prefix_end_idx = 0

        n1 = len(str1)
        n2 = len(str2)
        prefix_last_possible_idx = min(n1, n2)

        while (
            prefix_end_idx < prefix_last_possible_idx
            and str1[prefix_end_idx] == str2[prefix_end_idx]
        ):
            prefix_end_idx += 1

        # NOTE: There are easy meaningful optimizations we can make in
        # this loop. They won't increase the asymptotic efficiency, but
        # they will increase the efficiency by large constant factors. I
        # just don't have time to think about + implement them right
        # now. Wanted to do a quick problem before leaving.
        while prefix_end_idx > 0:
            prefix = str1[:prefix_end_idx]

            if (
                n1 % prefix_end_idx == n2 % prefix_end_idx == 0
                and str1 == prefix * (n1 // prefix_end_idx)
                and str2 == prefix * (n2 // prefix_end_idx)
            ):
                return prefix

            prefix_end_idx -= 1

        # prefix_end_idx == 0
        return ""


# @leet end
