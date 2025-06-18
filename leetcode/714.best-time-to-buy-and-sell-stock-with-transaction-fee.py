# @leet start
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # NOTE: Need ChatGPT to give me the gist of this one
        #
        # For each day we consider the maximum profit we can make in one
        # of two states:
        #
        # - having a stock at the end of the day (call this invested)
        # - not having a stock at the end of the day (call this
        # divested)
        invested_max_profit = -prices[0]
        divested_max_profit = 0

        for price in prices[1:]:
            # Choose the maximum of
            # - the maximum we make from being invested and holding the
            # stock
            # - the maximum we make from being divested and buying this
            # stock
            invested_max_profit = max(invested_max_profit, divested_max_profit - price)

            # Choose the maximum of
            # - the maximum we make from being divested and staying
            # divested
            # - the maximum we make from being invested and selling this
            # stock
            divested_max_profit = max(
                divested_max_profit, invested_max_profit + price - fee
            )

        return divested_max_profit


# @leet end
