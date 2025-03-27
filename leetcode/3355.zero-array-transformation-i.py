# @leet start
from collections import defaultdict
import itertools
import math


class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        # For each inclusive start point and exclusive end point of a
        # query, find how many query intervals overlap that point. (For
        # this problem a "point" is synonymous with an index of nums.)
        # We do this using a sweep line and prefix sum.
        change_point_dict: defaultdict[int, int] = defaultdict(int)

        for start, end in queries:
            change_point_dict[start] += 1
            change_point_dict[end + 1] -= 1

        # Indices of sorted_points and num_overlapping_at_points
        # correspond to each other. You can think of the two together as
        # functioning as a sorted dictionary.
        sorted_change_points = sorted(change_point_dict)
        num_overlapping_at_change_points = list(
            itertools.accumulate(change_point_dict[x] for x in sorted_change_points)
        )

        # Now check whether each number is less than or equal to the
        # number of intervals it overlaps with
        if sorted_change_points[0] == 0:
            change_point_idx = 0
            num_overlapping = num_overlapping_at_change_points[0]
        else:
            change_point_idx = -1
            num_overlapping = 0

        # Note: we don't need to worry about indexing out of bounds here
        # because there are at least 2 change points
        next_change_point = sorted_change_points[change_point_idx + 1]

        for point, num in enumerate(nums):
            # Update the number of overlapping intervals if necessary
            if point == next_change_point:
                change_point_idx += 1
                num_overlapping = num_overlapping_at_change_points[change_point_idx]

                try:
                    next_change_point = sorted_change_points[change_point_idx + 1]
                except IndexError:
                    next_change_point = math.inf

            # If the number is greater than the number of overlapping
            # intervals, it is impossible to form a zero array using the
            # given queries
            if num > num_overlapping:
                return False

        return True


# @leet end
