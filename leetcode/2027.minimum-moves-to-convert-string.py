# @leet start
class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)

        i = 0
        moves_taken = 0

        while i < n:
            if s[i] == "X":
                # Do a move on this and the next two elements
                moves_taken += 1

                i += 3
            else:
                # Move to the next element
                i += 1

        return moves_taken


# @leet end
