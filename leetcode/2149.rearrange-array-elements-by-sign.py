# @leet start
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        pos_count = 0
        neg_count = 0

        for num in nums:
            if num > 0:
                result[2 * pos_count] = num
                pos_count += 1
            else:
                result[1 + 2 * neg_count] = num
                neg_count += 1

        return result


# @leet end
