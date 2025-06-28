# @leet start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1

        max_value = 1

        for i in range(2, n + 1):
            nums[i] = nums[i // 2]

            if i % 2 == 1:
                nums[i] += nums[i // 2 + 1]

                max_value = nums[i]

        return max_value


# @leet end
