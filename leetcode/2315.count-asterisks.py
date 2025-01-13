# @leet start
class Solution:
    def countAsterisks(self, s: str) -> int:
        # Keep track of whether we're in a pair of |s or not
        in_pair = False

        # Keep track of number of asterisks outside of a pair of |s
        num_asterisks = 0

        for ch in s:
            if ch == "*" and not in_pair:
                num_asterisks += 1

            if ch == "|":
                in_pair = not in_pair

        return num_asterisks


# @leet end
