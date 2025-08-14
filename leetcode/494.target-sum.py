# @leet start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # dp[c] tells the number of ways we can assign + and -s among
        # the first i elements (the iteration count of the outer loop
        # below) to reach a sum of c
        dp = {0: 1}

        for num in nums:
            next_dp: dict[int, int] = {}

            for sum_, count in dp.items():
                next_dp[sum_ + num] = count + next_dp.get(sum_ + num, 0)
                next_dp[sum_ - num] = count + next_dp.get(sum_ - num, 0)

            dp = next_dp

        return dp.get(target, 0)


# @leet end
