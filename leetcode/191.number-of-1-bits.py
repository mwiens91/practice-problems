# @leet start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


# @leet end
