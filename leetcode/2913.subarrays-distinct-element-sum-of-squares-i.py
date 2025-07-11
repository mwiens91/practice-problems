# @leet start
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        # There are cleverer solutions to this. One involves doing
        # something similar to a sliding window. There's also something
        # called "Mo's algorithm" which might apply here, although
        # apparently it's a bit complicated.
        n = len(nums)
        result = 0

        for i in range(n):
            seen: set[int] = set()

            for j in range(i, n):
                seen.add(nums[j])
                result += len(seen) ** 2

        return result


# @leet end
