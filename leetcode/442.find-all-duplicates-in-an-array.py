# @leet start
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # NOTE: Used ChatGPT for a hint. Very clever solution.
        result: list[int] = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                result.append(idx + 1)

        return result


# @leet end
