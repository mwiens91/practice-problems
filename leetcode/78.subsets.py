# @leet start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        curr: list[int] = []

        def backtrack(i: int) -> None:
            if i == len(nums):
                res.append(curr[:])

                return

            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)

        backtrack(0)

        return res


# @leet end
