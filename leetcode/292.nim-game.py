# @leet start
class Solution:
    def canWinNim(self, n: int) -> bool:
        # We lose if the opponent can bring the stone total to 4 while
        # having it be our turn, otherwise we can win. Suppose there are
        # 4*k stones, for some positive integer k. Then regardless of
        # how many stones we take, the opponent can ensure 4 stones are
        # taken per round, and eventually win. However if there are
        # 4*k + m stones, where m = 1, 2, 3, then we can pick m stones
        # on the first turn, and then we're essentially starting a new
        # game with 4*k stones where the opponent starts first. We can
        # ensure 4 stones are taken per round, which will leave us with
        # <= 3 stones on our final turn in which we can win.
        return n % 4 != 0


# @leet end
