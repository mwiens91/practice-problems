# @leet start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Get length of prices list
        n = len(prices)

        # Do memoization: the keys are tuples containing an index to the
        # prices list and a boolean for whether we currently have a
        # stock Values are maximum profit.
        memo: dict[tuple[int, bool, bool], int] = {}

        # Note we never call this function when we're on cooldown (since
        # we can't do anything during this time anyway), so we don't
        # need to worry being on cooldown when we're inside the function
        def get_max_profit(idx: int, have_stock: bool) -> int:
            # Get result if we've already processed it
            try:
                return memo[(idx, have_stock)]
            except KeyError:
                pass

            # Handle index out of bounds
            if idx >= n:
                return 0

            # Get maximum profit
            if have_stock:
                # Try selling or not selling
                maximum_profit = max(
                    prices[idx] + get_max_profit(idx + 2, False),  # sell
                    get_max_profit(idx + 1, True),  # keep
                )
            else:
                # Try buying or not buying
                maximum_profit = max(
                    -prices[idx] + get_max_profit(idx + 1, True),  # buy
                    get_max_profit(idx + 1, False),  # don't
                )

            memo[(idx, have_stock)] = maximum_profit

            return maximum_profit

        return get_max_profit(0, False)


# @leet end
