# @leet start
import math


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # First sort coins; the list is length 12 at most, so this
        # operation is free
        coins.sort()

        # We'll memoize our solution: keys are amounts x and values are
        # minimum number of coins to reach x
        FAILURE_INT = -1

        memo: dict[int, int] = {0: 0}

        def get_min_coins_to_make_x(x: int) -> int:
            # Get memoized result
            if x in memo:
                return memo[x]

            # Compute result
            min_coins = math.inf

            # Try using each type of coin
            for coin in coins:
                if coin <= x:
                    # If using this coin is impossible, skip it
                    subproblem_min_coins = get_min_coins_to_make_x(x - coin)

                    if subproblem_min_coins == FAILURE_INT:
                        continue

                    # Update min
                    min_coins = min(min_coins, 1 + subproblem_min_coins)

            # Update memo and return result
            res = min_coins if min_coins != math.inf else FAILURE_INT
            memo[x] = res

            return res

        return get_min_coins_to_make_x(amount)


# @leet end
