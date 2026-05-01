# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_at_idx: dict[int, int] = {}

        for i, num in enumerate(nums):
            if target - num in seen_at_idx:
                return [i, seen_at_idx[target - num]]

            seen_at_idx[num] = i


# @leet end
