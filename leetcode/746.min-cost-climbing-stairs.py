# @leet start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Use dynamic programming to find the minimum cost to reach the
        # end starting from any given step
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


# @leet end
