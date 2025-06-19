# @leet start
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 1:
            return n

        return n // 2


# @leet end
