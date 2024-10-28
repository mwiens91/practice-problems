# @leet start
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price seen so far (so, in the past),
        # and the maximum profit we have been able to obtain so far
        min_price_seen = math.inf
        max_profit_seen = 0

        # Find max profit
        for price in prices:
            min_price_seen = min(min_price_seen, price)
            max_profit_seen = max(max_profit_seen, price - min_price_seen)

        return max_profit_seen
# @leet end
