# @leet start
from enum import Enum
import math


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # NOTE: needed to use Neetcode to figure out how to do this in
        # O(log(m + n)) time complexity. Note that the actual solution
        # has the even smaller time complexity O(log(min(m,n))).

        # We'll want to run a binary search on the smaller of the input
        # lists, so let's figure out which list is smaller
        if len(nums1) <= len(nums2):
            nums_smaller = nums1
            nums_larger = nums2
        else:
            nums_smaller = nums2
            nums_larger = nums1

        # Suppose for simplicity that m + n is odd. Then if we merged
        # both arrays of numbers, the median would be the middle number
        # such that an equal number of elements lie on both sides of it.
        # We can find this median without formally merging by
        # partitioning the smaller array into left and right partitions;
        # once this is chosen we automatically know how to partition the
        # larger array based on the size of the left and right
        # partitions of the smaller array. If the partitions satisfy the
        # property that every number on either left partition is <=
        # every number on either right partition, then the median is the
        # smallest number of the combined right partition (if we take
        # the rule that the right partition contains one greater element
        # than the left for m + n odd, which we will here). The idea is
        # that the combined left partition represents all elements to
        # the left of the median of the theoretically merged array,
        # while the combined right partition represents all elements to
        # the left of and including the median of the theoretically
        # merged array.
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

        # Define function to get values to the left and right of a
        # separator. The smaller boolean indicates whether to operate on
        # the smaller array or the larger one.
        def get_left_right_vals(
            idx: int, smaller: bool
        ) -> tuple[int | float, int | float]:
            nums = nums_smaller if smaller else nums_larger
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

        # Define a function which determines whether a given partition
        # is valid, or, if invalid, whether the left partition of the
        # smaller array is too small or too large. We let the smaller
        # separator index be as large as the length of the smaller
        # array, so we have #elements + 1 available separator positions.
        smaller_len = len(nums_smaller)
        larger_len = len(nums_larger)
        total_len = smaller_len + larger_len

        num_elements_in_left_partition = total_len // 2

        def get_larger_separator_idx(smaller_separator_idx: int) -> int:
            return num_elements_in_left_partition - smaller_separator_idx

        class PartitionResult(Enum):
            VALID = 1
            TOO_SMALL = 2
            TOO_LARGE = 3

        def get_partition_result(smaller_separator_idx: int) -> PartitionResult:
            smaller_left, smaller_right = get_left_right_vals(
                smaller_separator_idx, smaller=True
            )
            larger_left, larger_right = get_left_right_vals(
                get_larger_separator_idx(smaller_separator_idx), smaller=False
            )

            # If the maximum value of the left partition of the smaller
            # array is larger than the minimum value of the right
            # partition of the larger array, the left partition of the
            # smaller array is too large
            if smaller_left > larger_right:
                return PartitionResult.TOO_LARGE

            # Similarly, if the maximum value fo the left partition of
            # the smaller array is larger than the minimum value of the
            # right partition of the smaller array, the left partition
            # of the smaller array is too small
            if larger_left > smaller_right:
                return PartitionResult.TOO_SMALL

            # Partition is valid
            return PartitionResult.VALID

        # Now that we have the tools we need, we begin to find the
        # median. We can run a binary search on the smaller array to
        # find a valid partition. If there are many duplicate elements,
        # there may be more than one valid partition, but all valid
        # separator indices will be contiguous.
        left_idx = 0
        right_idx = smaller_len

        while True:
            mid_idx = (left_idx + right_idx) // 2

            partition_result = get_partition_result(mid_idx)

            if partition_result == PartitionResult.VALID:
                # It's valid, get out
                valid_smaller_sep_idx = mid_idx

                break

            if partition_result == PartitionResult.TOO_LARGE:
                right_idx = mid_idx - 1
            else:
                # The left partition is too small
                left_idx = mid_idx + 1

        # Now that we have a valid partition, we find the median. How we
        # compute it depends on whether the sum of both array lengths is
        # even or odd. We'll need the values on the left and right of
        # each separator.
        smaller_left, smaller_right = get_left_right_vals(
            valid_smaller_sep_idx, smaller=True
        )
        larger_left, larger_right = get_left_right_vals(
            get_larger_separator_idx(valid_smaller_sep_idx), smaller=False
        )

        if total_len % 2 == 1:
            # Odd. Median is smallest element of combined right
            # partitions.
            return float(min(smaller_right, larger_right))

        # Even. Median is average of largest of combined left
        # partitions and smallest of combined right partitions.
        return (max(smaller_left, larger_left) + min(smaller_right, larger_right)) / 2


# @leet end
