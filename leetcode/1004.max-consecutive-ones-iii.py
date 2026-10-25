# @leet start
from collections import deque


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeroIdxDeque = deque()
        start = 0
        best = 0

        for i, bit in enumerate(nums):
            if bit == 0:
                zeroIdxDeque.append(i)

            if len(zeroIdxDeque) > k:
                start = zeroIdxDeque.popleft() + 1

            best = max(best, i - start + 1)

        return best


# @leet end
