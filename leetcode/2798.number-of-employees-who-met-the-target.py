# @leet start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        return sum(1 for hour in hours if hour >= target)


# @leet end
