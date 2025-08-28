# @leet start
class Solution:
    def minPartitions(self, n: str) -> int:
        # Think of finding the solution by repeated subtraction of
        # deci-binary numbers from n. For all positive digits, we can
        # reduce their count by 1 by choosing a deci-binary number that
        # has 1 at that digit. Therefore, we can reduce n to 0 by adding
        # m demi-binary numbers where m is the maximum digit in n.
        return int(max(n))


# @leet end
