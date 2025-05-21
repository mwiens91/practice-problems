# @leet start
class Solution:
    def totalMoney(self, n: int) -> int:
        # The amount from the full weeks is given by the sum from i = 0
        # to i = num_full_weeks - 1 of 7 * (7 + 1) / 2 + 7 * i, which
        # simplifies to
        #
        # num_full_weeks * (49 + 7 * num_full_weeks) / 2
        num_full_weeks = n // 7
        amount_from_full_weeks = num_full_weeks * (49 + 7 * num_full_weeks) // 2

        # The amount from the last partial week is given by the sum from
        # i = 1 to i = num_days_remaining of num_full_weeks + i, which
        # simplifies to
        #
        # num_days_remaining
        # * (2 * num_full_weeks + num_days_remaining + 1) / 2
        num_days_remaining = n % 7
        amount_from_partial_week = (
            num_days_remaining * (2 * num_full_weeks + num_days_remaining + 1) // 2
        )

        return amount_from_full_weeks + amount_from_partial_week


# @leet end
