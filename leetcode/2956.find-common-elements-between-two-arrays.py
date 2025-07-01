# @leet start
class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ans1 = sum(1 for num in nums1 if num in nums2_set)
        ans2 = sum(1 for num in nums2 if num in nums1_set)

        return [ans1, ans2]


# @leet end
