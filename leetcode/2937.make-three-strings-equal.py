# @leet start
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_length = min(map(len, (s1, s2, s3)))

        # Find the first character at which the strings differ. If this
        # is the first character, we cannot make them equal, so we
        # return -1.
        if not s1[0] == s2[0] == s3[0]:
            return -1

        # i represents the prefix length for which all strings are equal
        i = 1

        while i < min_length:
            if not s1[i] == s2[i] == s3[i]:
                break

            i += 1

        return sum(len(s) - i for s in (s1, s2, s3))


# @leet end
