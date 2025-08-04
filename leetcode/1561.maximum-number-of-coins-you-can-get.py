# @leet start
class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        # For each triplet get the best two piles available and the
        # worst pile available: Alice gets the best pile, you get the
        # second best, and Bob gets the worst
        return sum(sorted(piles)[len(piles) // 3 :: 2])


# @leet end
