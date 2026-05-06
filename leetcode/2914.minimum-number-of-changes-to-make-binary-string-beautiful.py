# @leet start
class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(0, len(s), 2):
            changes += s[i] != s[i + 1]

        return changes


# @leet end
