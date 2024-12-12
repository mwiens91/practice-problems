# @leet start
class Solution:
    def rob(self, nums: list[int]) -> int:
        # Reuse solution to house robber I
        def house_robber_i(nums):
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

        # We can't rob both first and last house, so the best solution
        # will not never need to include both first and last house.
        # Therefore we can run the house robber I solution on all houses
        # excluding (1) the first house and (2) the last house, and then
        # take the maximum of these solutions.

        # However, first we need to deal with the edge case where
        # there's only one house
        if len(nums) == 1:
            return nums[0]

        # Deal with >= 2 houses
        return max(house_robber_i(nums[1:]), house_robber_i(nums[:-1]))


# @leet end
