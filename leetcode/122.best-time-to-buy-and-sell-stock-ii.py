# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # We'll take a greedy approach here. We'll buy on a day if we
        # can sell it the next day for a higher price, and do this for
        # every day this holds true.
        max_profit = 0

        for i in range(len(prices) - 1):
            max_profit += max(0, prices[i + 1] - prices[i])

        return max_profit


# @leet end
