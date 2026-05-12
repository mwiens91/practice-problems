# @leet start
class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda t: t[0] - t[1])
        total = 0
        curr = 0

        for spend, require in tasks:
            if require > curr:
                needed = require - curr
                curr += needed
                total += needed

            curr -= spend

        return total


# @leet end
