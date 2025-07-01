# @leet start
class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        # We store the hours seen mod 24
        hours_seen_counts = [0] * 24

        pair_count = 0

        for hour in hours:
            hour_remainder = hour % 24

            pair_count += hours_seen_counts[(24 - hour_remainder) % 24]
            hours_seen_counts[hour_remainder] += 1

        return pair_count


# @leet end
