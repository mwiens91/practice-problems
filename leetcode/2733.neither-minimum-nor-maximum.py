# @leet start
class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]

        for num in nums:
            if min_num < num < max_num:
                return num

            if num < min_num:
                if min_num < max_num:
                    return min_num

                min_num = num
            elif num > max_num:
                if min_num < max_num:
                    return max_num

                max_num = num

        return -1


# @leet end
