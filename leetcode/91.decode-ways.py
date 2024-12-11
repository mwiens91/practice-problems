# @leet start
class Solution:
    def numDecodings(self, s: str) -> int:
        # Put valid codes in a set
        VALID_CODES = set(str(x) for x in range(1, 27))

        # Now we'll figure out the solution with memoization. Since
        # we're trying to find the number of paths essentially we set
        # the end node (empty string) with a value of 1. The number of
        # ways a given string has is the number of different paths it
        # has to the end node.
        memo: dict[str, int] = {"": 1}

        def num_ways(str_: str) -> int:
            # Return memoized result
            try:
                return memo[str_]
            except KeyError:
                pass

            # Compute result
            res = 0

            if str_[0] in VALID_CODES:
                res += num_ways(str_[1:])

            if len(str_) > 1 and str_[0:2] in VALID_CODES:
                res += num_ways(str_[2:])

            memo[str_] = res

            return res

        return num_ways(s)


# @leet end
