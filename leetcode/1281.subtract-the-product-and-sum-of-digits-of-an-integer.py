# @leet start
from math import prod


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))

        return prod(digits) - sum(digits)


# @leet end
