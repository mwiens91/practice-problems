# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 1

        # Find the ways to get to the nth step given we started at first
        # step
        for _ in range(n - 1):
            curr, prev = curr + prev, curr

        return curr


# @leet end
