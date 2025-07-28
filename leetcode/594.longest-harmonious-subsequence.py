# @leet start
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)

        return max(
            (counts[num] + counts[num + 1] for num in counts if num + 1 in counts),
            default=0,
        )


# @leet end
