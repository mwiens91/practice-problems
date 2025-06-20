# @leet start
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda num: (bin(num).count("1"), num))


# @leet end
