# @leet start
class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        # Sort the costs in descending order. We can get every third
        # cost for free.
        cost.sort(reverse=True)

        return sum(cost) - sum(cost[i] for i in range(2, len(cost), 3))


# @leet end
