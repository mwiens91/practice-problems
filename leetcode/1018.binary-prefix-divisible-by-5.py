# @leet start
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result: list[bool] = []

        i = 0
        current_num = 0

        for num in nums:
            current_num = (current_num << 1) | num

            result.append(current_num % 5 == 0)

        return result


# @leet end
