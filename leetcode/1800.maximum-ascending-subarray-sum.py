# @leet start
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0

        current_sum = 0
        prev_num = 0

        for num in nums:
            if prev_num < num:
                current_sum += num
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = num

            prev_num = num

        max_sum = max(max_sum, current_sum)

        return max_sum


# @leet end
