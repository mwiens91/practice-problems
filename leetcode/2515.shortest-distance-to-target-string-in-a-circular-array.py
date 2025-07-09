# @leet start
class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        # We look to the left and right of the starting index and travel
        n = len(words)

        for i in range(n // 2 + 1):
            if target in {
                words[(startIndex + i) % n],
                words[(startIndex - i + n) % n] == target,
            }:
                return i

        return -1


# @leet end
