# @leet start
import math


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # NOTE: needed to use Neetcode to figure out how to do this in
        # O(log(m + n)) time complexity. Note that the actual solution
        # has the even smaller time complexity O(log(min(m,n))).

        # General idea: Suppose for simplicity that m + n is odd. Then
        # if we merged both arrays of numbers, the median would be the
        # middle number such that an equal number of elements lie on
        # both sides of it. We can find this median without formally
        # merging by partitioning the smaller array into left and right
        # partitions; once this is chosen we automatically know how to
        # partition the larger array based on the size of the left and
        # right partitions of the smaller array. If the partitions
        # satisfy the property that every number on either left
        # partition is <= every number on either right partition, then
        # the median is the smallest number of the combined right
        # partition (if we take the rule that the right partition
        # contains one greater element than the left for m + n odd,
        # which we will here). The idea is that the combined left
        # partition represents all elements to the left of the median of
        # the theoretically merged array, while the combined right
        # partition represents all elements to the left of and including
        # the median of the theoretically merged array.
        #
        # Let's look at an example. Suppose the smaller array was
        #
        # 2 3 4
        #
        # and the larger array was
        #
        # 1 4 5 7.
        #
        # If we partition the smaller array as
        #
        # 2 | 3 4
        #
        # then since m + n = 7, 3 elements must lie on each side of the
        # median in the theoretical merged array. Thus the larger array
        # must be partitioned as
        #
        # 1 4 | 5 7.
        #
        # A given partition is valid if all elements in the left
        # partitions are less than or equal to all elements in the right
        # partitions. In this case the partitioning scheme shown above
        #
        # 2   | 3 4
        # 1 4 | 5 7
        #
        # is not valid because 4 > 3 but 4 is part of the left
        # partitions and 3 is part of the right partitions. Instead, a
        # valid partitioning scheme would be
        #
        # 2 3 | 4
        # 1   | 4 5 7.
        #
        # We can find a valid partitioning scheme efficiently by running
        # a binary search on the smaller array. Let s_l, s_r be the
        # values to the left and right of the smaller array separator,
        # and let l_l, l_r be the corresponding values for the larger
        # array.
        #
        # If l_s > r_l, then we know the left partition of the smaller
        # array is too large, and we need to move the separator to the
        # left. If l_l > r_s, then there we need to move the separator
        # to the right. If neither of those conditions are true, then a
        # partition is valid.

        # Determine which array is smaller and which is larger
        if len(nums1) <= len(nums2):
            nums_smaller = nums1
            nums_larger = nums2
        else:
            nums_smaller = nums2
            nums_larger = nums1

        # This function gets values to the left and right of a
        # separator. For separators that lie at either end of an array,
        # we define the boundary conditions to the left to be -infinity
        # and to the right to be positive infinity.
        def get_left_right_vals(
            idx: int, nums: list[int]
        ) -> tuple[int | float, int | float]:
            nums_len = len(nums)

            if idx > 0:
                left = nums[idx - 1]
            else:
                left = -math.inf

            if idx < nums_len:
                right = nums[idx]
            else:
                right = math.inf

            return (left, right)

        # Define convenience functions to call get_left_right_vals for
        # each array
        smaller_len = len(nums_smaller)
        total_len = smaller_len + len(nums_larger)

        combined_left_partition_size = total_len // 2

        def get_smaller_left_right_vals(
            smaller_separator_idx: int,
        ) -> tuple[int | float, int | float]:
            return get_left_right_vals(smaller_separator_idx, nums_smaller)

        def get_larger_left_right_vals(
            smaller_separator_idx: int,
        ) -> tuple[int | float, int | float]:
            larger_separator_idx = (
                combined_left_partition_size - smaller_separator_idx
            )

            return get_left_right_vals(
                larger_separator_idx, nums_larger
            )

        # Run a binary search on the smaller array to find a valid
        # partition
        left_idx = 0
        right_idx = smaller_len

        while True:
            mid_idx = (left_idx + right_idx) // 2

            # Get values to the left and right of each array's separator
            smaller_left, smaller_right = get_smaller_left_right_vals(mid_idx)
            larger_left, larger_right = get_larger_left_right_vals(mid_idx)

            # Determine how to proceed with the binary search
            if smaller_left > larger_right:
                # Too many values in left partition of smaller array
                right_idx = mid_idx - 1
            elif larger_left > smaller_right:
                # Too few values in left partition of smaller array
                left_idx = mid_idx + 1
            else:
                # Valid, get out
                break

        # Now find the median. How we compute it depends on whether the
        # sum of both array lengths is even or odd. We'll need the
        # values on the left and right of each separator, but we already
        # have those in scope from the above code.
        if total_len % 2 == 1:
            # Odd. Median is smallest element of combined right
            # partitions.
            return float(min(smaller_right, larger_right))

        # Even. Median is average of largest of combined left
        # partitions and smallest of combined right partitions.
        return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2


# @leet end
