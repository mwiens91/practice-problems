# @leet start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Use two pointers, i will keep moving forward until we find the
        # first character of needle; once and if that is found j will
        # traverse needle and haystack simulataneously looking for a
        # match. If a match is found, we return i; else we keep moving i
        # forward.
        #
        # Note that we can't just set i to j after a potential match
        # fails. See the following example:
        #
        # needle: loele
        # haystack substring: loeloele
        #                     ^   ^
        #                     i   j
        # Setting i to j after the initial match fails causes us to miss
        # the actual first occurance.
        len_haystack = len(haystack)
        len_needle = len(needle)

        # Edge case
        if len_needle > len_haystack:
            return -1

        for i in range(len_haystack - len_needle + 1):
            # Check for a potential match
            try:
                haystack_ch = haystack[i]

                if haystack_ch == needle[0]:
                    # See if the rest is a match
                    for j in range(1, len(needle)):
                        assert haystack[i + j] == needle[j]

                    # We got a match!
                    return i

            except AssertionError:
                pass

        # Failed to find occurance of needle in haystack
        return -1


# @leet end
