# @leet start
from bisect import bisect_left

def find_pivot(i, j, nums):
    """Return the pivot k.

    i is the starting index of subarray we're looking at; j is the
    ending index; both inclusive. Here we assume that i < j. We'll
    handle i == j elsewhere. (i > j should never happen.)

    The pivot k is given by k = n - j whenever we reach a base case. If
    the array isn't rotated, we just return None.
    """
    # Base case
    if j == i + 1:
        if nums[j] < nums[i]:
            # Found pivot k
            return len(nums) - j

        # No pivot k
        return None

    # Middle point of subarray nums[i:j] (j inclusive)
    mid_idx = i + (j - i) // 2

    # Recurse
    if nums[i] > nums[mid_idx]:
        return find_pivot(i, mid_idx, nums)

    return find_pivot(mid_idx, j, nums)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Find pivot k
        nums_length = len(nums)

        # No rotation possible for length 1 array
        if nums_length == 1:
            k = None
        else:
            k = find_pivot(0, nums_length - 1, nums)

        # Now bisect to find if target is in nums. Which subarray we
        # search in depends on the rotation.
        lo = 0
        hi = nums_length

        if k is None:
            # Search whole array
            pass
        elif target <= nums[nums_length - 1]:
            # Search the beginning part of the non-rotated array
            lo = nums_length - k
        else:
            # Search the ending part of the non-rotated array
            hi = nums_length - k

        # target_idx is where target *should* be if it's in the array.
        # If target is greater than everything in the array then
        # target_idx will be whatever hi is set to.
        target_idx = bisect_left(nums, target, lo, hi)

        return target_idx if target_idx != hi and nums[target_idx] == target else -1
# @leet end
