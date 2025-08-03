# @leet start
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # Return whether Manhattan distance from a1 is even
        def is_white(coord: str) -> bool:
            return (ord(coord[0]) - ord("a") + int(coord[1]) - 1) % 2 == 0

        return is_white(coordinate1) == is_white(coordinate2)


# @leet end
