# @leet start
import math


class Solution:
    def countBits(self, n: int) -> list[int]:
        # Deal with edge case: n == 0
        if n == 0:
            return [0]

        # Keep all results in a list. We'll generate more results than we
        # need but return only the required amount. We'll also re-use
        # results from the previous power of two, initialized to the results
        # of 2^0.
        results = [0, 1]
        intermediate_results = [1]

        for _ in range(math.ceil(math.log2(n))):
            intermediate_results += [x + 1 for x in intermediate_results]

            results += intermediate_results

        return results[: n + 1]


# @leet end
