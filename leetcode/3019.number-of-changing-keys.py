# @leet start
class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(s[i + 1].lower() != s[i].lower() for i in range(0, len(s) - 1))


# @leet end
