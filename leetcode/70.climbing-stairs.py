# @leet start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Give the solution if n is a base case
        if n == 1:
            return 1

        if n == 2:
            return 2

        # Use a bottom-up solution
        num_ways = [0] * (n + 1)
        num_ways[1] = 1
        num_ways[2] = 2

        for i in range(3, n + 1):
            num_ways[i] = num_ways[i - 1] + num_ways[i - 2]

        return num_ways[n]
# @leet end
