# @leet start
from itertools import accumulate


class NumArray:

    def __init__(self, nums: list[int]):
        # Get cumulative sums
        self.cumulative_sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.cumulative_sums[right] - self.cumulative_sums[left - 1]

        return self.cumulative_sums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @leet end
