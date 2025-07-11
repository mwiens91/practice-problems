# @leet start
class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        count = 0

        for percent in batteryPercentages:
            if percent - count > 0:
                count += 1

        return count


# @leet end
