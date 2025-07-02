# @leet start
class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        taxes = 0
        prev_upper_bound = 0

        for upper_bound, percent in brackets:
            if income <= prev_upper_bound:
                break

            taxes += (min(income, upper_bound) - prev_upper_bound) * percent / 100
            prev_upper_bound = upper_bound

        return taxes


# @leet end
