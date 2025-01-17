# @leet start
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # For each kid, see if the number of candies they have could
        # have after being given the extra candies is at least as large
        # as the maximum number of candies any child has (not including
        # any extras)
        result: list[bool] = [False] * len(candies)

        max_candies = max(candies)

        for i, num_candies in enumerate(candies):
            if num_candies + extraCandies >= max_candies:
                result[i] = True

        return result


# @leet end
