# @leet start
class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        # Get the sum of each list after replacing all of the zeros by
        # 1s
        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)

        nums1_sum = sum(nums1) + nums1_zeros
        nums2_sum = sum(nums2) + nums2_zeros

        # Create variables based on the relative sizes of the sums
        (_, smaller_has_zero), (larger_sum, _) = sorted(
            ((nums1_sum, bool(nums1_zeros)), (nums2_sum, bool(nums2_zeros)))
        )

        # If the sums are not equal and there is no zero available for
        # the smaller sum to equalize the sums, this is impossible
        if not smaller_has_zero and nums1_sum != nums2_sum:
            return -1

        # Return the smallest possible sum
        return larger_sum


# @leet end
