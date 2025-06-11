# @leet start
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # Sort the distinct numbers
        nums.sort()

        # Count the number of ways to get each index value of the "dp"
        # list
        dp = [0] * (target + 1)
        dp[0] = 1

        for current_target in range(1, target + 1):
            for num in nums:
                if num > current_target:
                    break

                dp[current_target] += dp[current_target - num]

        return dp[target]


# @leet end
