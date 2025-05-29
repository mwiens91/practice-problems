# @leet start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        # There's probably a nice formula we can come up with here, but
        # the constraints on n are so small that we can just simulate this
        matches = 0

        while n > 1:
            matches += n // 2

            if n % 2 == 0:
                n //= 2
            else:
                n = n // 2 + 1

        return matches


# @leet end
