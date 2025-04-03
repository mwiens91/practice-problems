# @leet start
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        # NOTE: this is the same problem as LC 2873, but with harder
        # constraints. I did an O(n) time & memory complexity solution
        # there and talked about how I could bring it down to O(1)
        # memory. I'll implement that idea here.

        # We'll iterate over the last element of the triplet, and update
        # the maximum triplet value seen. Then we'll use the value we
        # iterate over to update the maximum difference and maximum
        # number we've seen so far; the order is important here because
        # we need to use the *previously* seen maximum number to update
        # the maximum difference, using the value we iterate over as the
        # subtracting term.
        max_triplet_val = 0
        max_difference = nums[0] - nums[1]
        max_num_seen = max(nums[0], nums[1])

        for k in range(2, len(nums)):
            # Update the maximum triplet value
            max_triplet_val = max(max_triplet_val, max_difference * nums[k])

            # Use this value to update the other variables for the next
            # iteration
            max_difference = max(max_difference, max_num_seen - nums[k])
            max_num_seen = max(max_num_seen, nums[k])

        return max_triplet_val


# @leet end
