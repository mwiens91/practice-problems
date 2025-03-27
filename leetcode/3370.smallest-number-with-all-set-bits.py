# @leet start
import math


class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2 ** (math.floor(math.log2(n)) + 1) - 1


# @leet end
