# @leet start
import itertools


class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        count = 0

        for num1, num2 in itertools.product(nums1, nums2):
            if num1 % (num2 * k) == 0:
                count += 1

        return count


# @leet end
