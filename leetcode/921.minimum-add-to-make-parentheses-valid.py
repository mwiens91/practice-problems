# @leet start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        opened = 0

        for ch in s:
            if ch == ")":
                if opened:
                    opened -= 1
                else:
                    count += 1
            else:
                opened += 1

        return count + opened


# @leet end
