# @leet start
class Solution:
    def occurrencesOfElement(
        self, nums: list[int], queries: list[int], x: int
    ) -> list[int]:
        n = len(nums)
        count = 0

        for i in range(n):
            num = nums[i]
            nums[i] = -1

            if num == x:
                nums[count] = i
                count += 1

        return [nums[q - 1] if q <= n else -1 for q in queries]


# @leet end
