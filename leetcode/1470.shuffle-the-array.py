# @leet start
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        # I can't think of a way to do this in O(1) space, so instead we
        # use O(n)
        result: list[int] = []

        for xi, yi in zip(nums[:n], nums[n:]):
            result.extend([xi, yi])

        return result


# @leet end
