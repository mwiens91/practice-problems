# @leet start
class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # n - 1 is the number of passes it takes to get from one
        # end to the the other
        k %= 2 * (n - 1)

        if k < (n - 1):
            return k

        return 2 * (n - 1) - k


# @leet end
