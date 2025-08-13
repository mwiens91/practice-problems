# @leet start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        seen: list[int] = set()
        ops = 0

        for num in reversed(nums):
            ops += 1

            if num <= k and num not in seen:
                seen.add(num)

                if len(seen) == k:
                    return ops


# @leet end
