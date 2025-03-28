# @leet start
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # Count how many smaller numbers there are than each num
        smaller_than_counts = {}

        for i, num in enumerate(sorted(nums)):
            if num not in smaller_than_counts:
                smaller_than_counts[num] = i

        # Return the counts for each element in the original ordering of
        # nums
        return [smaller_than_counts[num] for num in nums]


# @leet end
