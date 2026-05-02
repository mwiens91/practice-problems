# @leet start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []

        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)

        return res


# @leet end
