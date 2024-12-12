# @leet start
class Solution:
    def rob(self, nums: list[int]) -> int:
        # Get length of nums
        n = len(nums)

        # Use memoization here. Put the last house and the only out of
        # bounds house that we would attempt to rob in the memo now to
        # simplify the recursive function below.
        memo: dict[int, int] = {n - 1: nums[n - 1], n: 0}

        def get_max_profit(idx: int) -> int:
            # Use precomputed result
            if idx in memo:
                return memo[idx]

            # We take the option of either robbing a house or not robbing
            # it and moving to the next one
            max_profit = max(
                nums[idx] + get_max_profit(idx + 2), get_max_profit(idx + 1)
            )

            memo[idx] = max_profit

            return max_profit

        return get_max_profit(0)


# @leet end
