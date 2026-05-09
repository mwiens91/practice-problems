# @leet start
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        prefix_mins = nums[:]

        for i in range(1, n):
            prefix_mins[i] = min(prefix_mins[i - 1], nums[i])

        suffix_stack: list[int] = []  # monotonically decreasing

        for i in range(n - 1, 0, -1):
            while suffix_stack and suffix_stack[-1] <= prefix_mins[i - 1]:
                suffix_stack.pop()

            if suffix_stack and prefix_mins[i - 1] < suffix_stack[-1] < nums[i]:
                return True

            if nums[i] > prefix_mins[i - 1] and (
                not suffix_stack or nums[i] < suffix_stack[-1]
            ):
                suffix_stack.append(nums[i])

        return False


# @leet end
