# @leet start
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        unique_types = len(set(candyType))

        return min(unique_types, n // 2)


# @leet end
