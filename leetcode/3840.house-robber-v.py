# @leet start
class Solution:
    def rob(self, nums: list[int], colors: list[int]) -> int:
        n = len(nums)

        second_last = 0
        last = nums[0]

        for i in range(1, n):
            curr = nums[i]

            if colors[i] != colors[i - 1]:
                curr += last
            else:
                curr += second_last

            second_last = last
            last = max(curr, last)

        return last


# @leet end
