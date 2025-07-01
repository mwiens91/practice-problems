# @leet start
from operator import itemgetter


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num_strs = [str(num).zfill(4) for num in (num1, num2, num3)]

        return int("".join(min(map(itemgetter(i), num_strs)) for i in range(4)))


# @leet end
