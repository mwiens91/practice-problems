# @leet start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ((ord(coordinates[0]) - ord("a")) + int(coordinates[1])) % 2 == 0


# @leet end
