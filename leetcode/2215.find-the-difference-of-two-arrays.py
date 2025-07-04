# @leet start
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return [list(nums1_set - nums2_set), list(nums2_set - nums1_set)]


# @leet end
