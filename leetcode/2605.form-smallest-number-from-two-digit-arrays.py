# @leet start
class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        # If the two lists have a non-empty intersection, return the
        # smallest element in the intersection. Otherwise, get the
        # minimum of both lists and return a number containing the
        # smallest of the mins in the 10s digit and the larger of the
        # mins in the 1s digit
        if intersection := set(nums1) & set(nums2):
            return min(intersection)

        smaller_min, larger_min = sorted(map(min, (nums1, nums2)))

        return smaller_min * 10 + larger_min


# @leet end
