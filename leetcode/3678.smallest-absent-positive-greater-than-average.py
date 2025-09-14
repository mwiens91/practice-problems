# @leet start
class Solution:
    def smallestAbsent(self, nums: list[int]) -> int:
        nums_set = set(nums)

        # Get the smallest positive integer larger than the mean
        candidate = max(0, int(sum(nums) / len(nums))) + 1

        while candidate in nums_set:
            candidate += 1

        return candidate


# @leet end
