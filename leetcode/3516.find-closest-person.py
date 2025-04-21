# @leet start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        diff = abs(x - z) - abs(y - z)

        if diff == 0:
            return 0

        if diff < 0:
            return 1

        return 2


# @leet end
