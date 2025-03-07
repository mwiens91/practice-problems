# @leet start
class Solution:
    def stoneGame(self, piles: list[int]) -> bool:  # pylint: disable=unused-argument
        # The sum of piles is odd, meaning one player will end up with
        # more stones in any partitioning of stones. Alice goes first,
        # and she can force the picks in such a way sthat she can choose
        # either all even indexed stones or odd indexed stones. One of
        # the sume of even indexed stones or odd indexed stones is
        # larger than the other, so Alice can always win.
        return True


# @leet end
