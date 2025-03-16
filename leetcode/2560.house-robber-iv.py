# @leet start
class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        # Count number of houses
        num_houses = len(nums)

        # Define a function to determine if we can steal from k homes
        # and have a capability less than or equal to a target value. We
        # can do this in a greedy way by going through each house in
        # order, and if it less than or equal to target, we steal from
        # it and skip the next house, or don't steal and continue with
        # the next house.
        def can_have_capability_at_most_target(target: int) -> bool:
            num_houses_robbed = 0

            i = 0

            while i < num_houses:
                # Try robbing from a house
                if nums[i] <= target:
                    num_houses_robbed += 1

                    i += 2
                else:
                    i += 1

                # Check if we've robbed k houses
                if num_houses_robbed >= k:
                    return True

            # Failed to rob k houses
            return False

        # Do a binary search to find the minimum capability we can
        # achieve
        possible_targets_sorted = sorted(nums)

        left = 0
        right = num_houses - 1

        while left <= right:
            mid = (left + right) // 2
            target = possible_targets_sorted[mid]

            if can_have_capability_at_most_target(target):
                right = mid - 1
            else:
                left = mid + 1

        return possible_targets_sorted[left]


# @leet end
