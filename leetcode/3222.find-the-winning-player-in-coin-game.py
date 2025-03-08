# @leet start
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # The number of rounds is limited by either exhausting x coins
        # or groups of 4 y coins
        num_rounds = min(x, y // 4)

        # Since Alice starts first, if she performs the last round, she
        # wins; otherwise she loses.
        if num_rounds % 2 == 1:
            return "Alice"

        return "Bob"


# @leet end
