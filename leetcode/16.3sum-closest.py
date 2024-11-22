# @leet start
import math


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Initialize a closest sum and an associated difference we'll
        # update as we continue along
        closest_sum_to_target = None
        closest_sum_to_target_diff = math.inf

        # Sort the input, this lets us do our main solution in O(n^2)
        # time instead of O(n^3)
        nums.sort()

        # Now we'll fix each number x as a pivot, and have an effective
        # target
        #
        # effective target = target - x.
        #
        # Then we'll use a two-pointer technique to find the closest
        # sum to the effective target.
        n = len(nums)

        for pivot_idx, pivot in enumerate(nums[:-2]):
            effective_target = target - pivot

            left = pivot_idx + 1
            right = n - 1

            # Keep track of the difference between the effective target
            # and the closest sum we've come up with to the effective
            # target. Keep track of the indices that resulted in the
            # minimum difference.
            closest_sum_to_effective_target_diff = math.inf
            best_left = None
            best_right = None

            # Do the two pointer technique
            while left < right:
                # Get sum and update the diff
                current_two_sum = nums[left] + nums[right]
                current_two_sum_diff = abs(effective_target - current_two_sum)

                if current_two_sum_diff < closest_sum_to_effective_target_diff:
                    closest_sum_to_effective_target_diff = current_two_sum_diff
                    best_left = left
                    best_right = right

                # Move pointers
                if current_two_sum == effective_target:
                    # If it's equal get out of this loop and we'll
                    # short-circuit this solution in a few lines
                    break

                if current_two_sum > effective_target:
                    right -= 1
                else:
                    left += 1

            # Use the closest sum to the effective target difference to
            # update the closest sum to the real target
            temp_sum = pivot + nums[best_left] + nums[best_right]
            temp_diff = abs(target - temp_sum)

            # If we hit the target, get out early
            if temp_diff == 0:
                return temp_sum

            # Update if we've improved on what we had before
            if temp_diff < closest_sum_to_target_diff:
                closest_sum_to_target = temp_sum
                closest_sum_to_target_diff = temp_diff

        return closest_sum_to_target


# @leet end
