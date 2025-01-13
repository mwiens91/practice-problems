# @leet start
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Handle n <= 0
        if n <= 0:
            return False

        # Handle n > 0
        log_n4 = math.log(n, 4)

        return log_n4 == int(log_n4)


# @leet end
