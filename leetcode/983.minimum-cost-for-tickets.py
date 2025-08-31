# @leet start
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (days[-1] + 1)

        travel_day_idx = 0

        for day in range(1, days[-1] + 1):
            if travel_day_idx < len(days) and day == days[travel_day_idx]:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )

                travel_day_idx += 1
            else:
                dp[day] = dp[day - 1]

        return dp[days[-1]]


# @leet end
