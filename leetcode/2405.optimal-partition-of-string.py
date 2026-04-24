# @leet start
class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        seen: set[str] = set()

        for ch in s:
            if ch in seen:
                count += 1
                seen = set()

            seen.add(ch)

        return count


# @leet end
