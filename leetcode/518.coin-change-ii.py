# @leet start
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # This is a simple dynamic programming problem. First sort the
        # coins in ascending order so we can optimize code below.
        coins.sort()

        # We can memoize by recording how many combinations there are to
        # reach a target starting from a given index.
        memo: dict[tuple[int, int], int] = {}

        last_index = len(coins) - 1

        def get_num_combinations(idx: int, target: int) -> int:
            # Try using memo
            if (idx, target) in memo:
                return memo[(idx, target)]

            # Base case: we met target
            coin_value = coins[idx]

            if coin_value == target:
                return 1

            # Optimization: if this coin is bigger than the target, than
            # all subsequent coins will be bigger too
            if coin_value > target:
                return 0

            # Count number of combinations
            num_combinations = 0

            # Try taking one of the current coin if possible
            if coin_value < target:
                num_combinations += get_num_combinations(idx, target - coin_value)

            # Try not taking the coin
            if idx < last_index:
                num_combinations += get_num_combinations(idx + 1, target)

            # Memoize and return
            memo[(idx, target)] = num_combinations

            return num_combinations

        # Deal with edge case: amount == 0. Otherwise use the dynamic
        # programming solution.
        if amount == 0:
            return 1

        return get_num_combinations(0, amount)


# @leet end
