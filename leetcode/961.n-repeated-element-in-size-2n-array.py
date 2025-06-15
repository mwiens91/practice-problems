# @leet start
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # Find the first character to be repeated twice
        seen: set[int] = set()

        for num in nums:
            if num in seen:
                return num

            seen.add(num)


# @leet end
