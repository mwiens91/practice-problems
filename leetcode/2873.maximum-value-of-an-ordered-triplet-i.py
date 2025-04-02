# @leet start
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        # Find maximums of prefix and suffix arrays
        n = len(nums)

        prefix_maxes = [nums[0]] * n
        suffix_maxes = [nums[-1]] * n

        for i in range(1, n):
            prefix_maxes[i] = max(prefix_maxes[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            suffix_maxes[i] = max(suffix_maxes[i + 1], nums[i])

        # Now find the maximum triplet value, iterating over every
        # middle index of the triplet
        max_triplet_val = 0

        for i in range(1, n - 1):
            max_triplet_val = max(
                max_triplet_val, (prefix_maxes[i - 1] - nums[i]) * suffix_maxes[i + 1]
            )

        # NOTE: we should also be able to do this in O(1) memory by
        # iterating over the final element of the triplet instead of the
        # middle element. It'd a bit tricker to implement, but the idea
        # is to keep track of the maximum of the minimum seen from the
        # left so far in two variables; the trick is to make sure the
        # maximum occurs before the minimum.
        return max_triplet_val


# @leet end
